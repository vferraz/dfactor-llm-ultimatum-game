#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch wrapper for running LLM ultimatum game experiments.

Orchestrates multiple (game, model) runs of run_sim_tokens1.py,
collecting results into a structured output directory with a
manifest TSV for tracking completed runs.

Usage:
    python run_batch_wrapper.py --games PdPd,AsAs --rounds 100 \\
        --models mistralai/Mistral-Nemo-Base-2407 Qwen/Qwen2.5-32B
"""

import argparse
import datetime as dt
import glob
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import List

# -------- config you might tweak once and forget --------
# These stay constant across runs unless overridden by flags.
DEFAULT_FLAGS = [
    "--baseline",
    "--history",
    "--layer", "all",
    "--use_ln_f_all",
    "--device_map", "auto",
    "--shuffle_valid_moves",
    # "--save_token_layers",   # uncomment if you always want token layers
]
SCRIPT_NAME = "run_sim_tokens1.py"
# -------------------------------------------------------


def model_alias(model_id: str) -> str:
    """
    Sanitize a Hugging Face model id (e.g., 'Qwen/Qwen2.5-32B-Instruct')
    into a filesystem-friendly alias: 'Qwen-Qwen2.5-32B-Instruct'
    """
    alias = model_id.strip()
    alias = alias.replace("/", "-")
    # Keep letters, numbers, dots, underscores, dashes; replace others with '-'
    alias = re.sub(r"[^A-Za-z0-9._-]+", "-", alias)
    alias = re.sub(r"-{2,}", "-", alias).strip("-")
    return alias


def find_single_parquet(run_dir: Path) -> Path:
    """Find the single results parquet produced by run_sim_tokens1.py in a run dir."""
    matches = sorted(run_dir.glob("results_*.parquet"))
    if len(matches) == 0:
        raise FileNotFoundError(f"No results_*.parquet in {run_dir}")
    if len(matches) > 1:
        # Pick the newest one
        matches = sorted(matches, key=lambda p: p.stat().st_mtime, reverse=True)
    return matches[0]


def run_one(
    project_root: Path,
    output_root: Path,
    logs_root: Path,
    game: str,
    rounds: int,
    model_id: str,
    extra_flags: List[str],
    python_bin: str = "python",
) -> Path:
    """
    Run a single (game, model) job and return the path to the copied final parquet.
    """
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    alias = model_alias(model_id)
    run_tag = f"{game}__{alias}__{ts}"

    # Command to run your existing simulation script
    cmd = [
        python_bin, str(project_root / SCRIPT_NAME),
        "--games", game,
        "--rounds", str(rounds),
        "--model_name", model_id,
        "--output_dir", str(output_root),
        "--run_tag", run_tag,
        *extra_flags,
    ]

    # Log file
    logs_root.mkdir(parents=True, exist_ok=True)
    log_path = logs_root / f"{run_tag}.log"
    with log_path.open("w", encoding="utf-8") as logf:
        logf.write("CMD: " + " ".join(cmd) + "\n\n")
        logf.flush()
        proc = subprocess.run(cmd, stdout=logf, stderr=subprocess.STDOUT, cwd=project_root)
        if proc.returncode != 0:
            raise RuntimeError(f"Job failed (see log): {log_path}")

    # Locate the parquet produced by run_sim_tokens1.py
    run_results_dir = output_root / run_tag
    parquet_src = find_single_parquet(run_results_dir)

    # Copy to a clean, friendly location
    final_dir = output_root / game / alias / ts
    final_dir.mkdir(parents=True, exist_ok=True)
    final_name = f"results_{game}__{alias}__{ts}.parquet"
    parquet_dst = final_dir / final_name
    shutil.copy2(parquet_src, parquet_dst)

    # Optionally, also copy the activations subdir from the script (keeps original structure)
    # They live under: output/activations/<run_tag>/...
    activ_src = output_root / "activations" / run_tag
    if activ_src.exists():
        activ_dst = final_dir / "activations"
        if activ_dst.exists():
            shutil.rmtree(activ_dst)
        shutil.copytree(activ_src, activ_dst)

    return parquet_dst


def main():
    ap = argparse.ArgumentParser(description="Batch wrapper for run_sim_tokens1.py")
    ap.add_argument("--games", required=True,
                    help="Comma-separated game codes (e.g., 'PdPd,AsAs')")
    ap.add_argument("--rounds", type=int, required=True,
                    help="Number of rounds per game")
    ap.add_argument("--models", nargs="+", required=True,
                    help="One or more HF model ids (e.g., mistralai/Mistral-Nemo-Base-2407 Qwen/Qwen2.5-32B)")
    ap.add_argument("--output_root", default="batch_output",
                    help="Root folder to store all runs and final copies")
    ap.add_argument("--python_bin", default="python",
                    help="Python executable to invoke (defaults to 'python' in the current venv)")
    ap.add_argument("--extra", nargs="*", default=[],
                    help="Extra flags to forward to run_sim_tokens1.py (advanced)")
    args = ap.parse_args()

    project_root = Path.cwd()
    output_root = (project_root / args.output_root).resolve()
    logs_root = output_root / "logs"

    # Compose the final constant flags
    extra_flags = DEFAULT_FLAGS + args.extra

    games = [g.strip() for g in args.games.split(",") if g.strip()]
    models = [m.strip() for m in args.models if m.strip()]

    print(f"Project:   {project_root}")
    print(f"Output to: {output_root}")
    print(f"Logs:      {logs_root}")
    print(f"Games:     {games}")
    print(f"Rounds:    {args.rounds}")
    print(f"Models:    {models}")
    print(f"Flags:     {extra_flags}")
    print()

    output_root.mkdir(parents=True, exist_ok=True)

    manifest_rows = []
    for model in models:
        for game in games:
            print(f"=== Running game={game} | model={model} ===")
            try:
                dst = run_one(
                    project_root=project_root,
                    output_root=output_root,
                    logs_root=logs_root,
                    game=game,
                    rounds=args.rounds,
                    model_id=model,
                    extra_flags=extra_flags,
                    python_bin=args.python_bin,
                )
                print(f"Saved: {dst}\n")
                manifest_rows.append(f"{game}\t{model}\t{dst}")
            except Exception as e:
                print(f"[ERROR] {game} | {model}: {e}\n")

    # Write a simple manifest for convenience
    manifest = output_root / f"manifest_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.tsv"
    manifest.write_text("game\tmodel\tparquet_path\n" + "\n".join(manifest_rows), encoding="utf-8")
    print(f"Manifest: {manifest}")


if __name__ == "__main__":
    main()
