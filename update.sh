#!/bin/zsh
# One-shot update: copy from vault → build → commit → push. Usage: ./update.sh "commit message"
set -e
cd "$(dirname "$0")"
python3 scripts/copy_from_vault.py
npx quartz build 2>&1 | grep -E "Found|Emitted|rror"
git add -A
git commit -q -m "${1:-Update draft $(date +%F)}"
git push
echo "Pushed. Live in ~1 min: https://jcutlerbiostats.github.io/self-certification-paper/"
