#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="$ROOT_DIR/metricx"

if [ -d "$TARGET_DIR/.git" ]; then
  echo "MetricX already present at $TARGET_DIR"
  exit 0
fi

if [ -d "$TARGET_DIR" ] && [ "$(ls -A "$TARGET_DIR")" ]; then
  echo "Directory exists and is not empty: $TARGET_DIR"
  echo "Please move/remove it, or clone manually into that path."
  exit 1
fi

git clone https://github.com/google-research/metricx.git "$TARGET_DIR"
echo "Cloned MetricX into $TARGET_DIR"