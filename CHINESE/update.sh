#!/bin/bash

# Define source and destination directories
SRC="$HOME/MANDARIN"
DEST="${1:-.}" # Defaults to the current directory if no destination is provided

if [ ! -d "$SRC" ]; then
    echo "Error: Source directory $SRC does not exist."
    exit 1
fi

echo "Syncing from $SRC to $DEST..."

# Rsync command using filter rules:
# - Includes the /audio directory and its contents
# - Includes all top-level .json files
# - Excludes everything else

rsync -avhm \
  --include="/audio" \
  --include="/audio/**" \
  --include="*.json" \
  --exclude="*" \
  "$SRC/" "$DEST/"

echo "Sync complete."
