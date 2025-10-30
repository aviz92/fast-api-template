#!/bin/bash
set -e

# usage: ./run_pytest_marker.sh MARKER [BRANCH]
MARKER="$1"
BRANCH="${2:-$(git rev-parse --abbrev-ref HEAD)}"

if [ -z "$MARKER" ]; then
  echo "Usage: $0 MARKER [BRANCH]"
  exit 1
fi

echo "Running Pytest workflow with:"
echo "  Marker: $MARKER"
echo "  Branch: $BRANCH"

gh workflow run "Pytest by Marker" \
  --ref "$BRANCH" \
  -f marker="$MARKER"
