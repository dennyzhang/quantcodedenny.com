#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME="denny/llm-stock-prompt"
TAG=${1:-latest}   # Allow overriding with ./publish.sh v1.0.0

# -----------------------------------------------------------------------------
# Build & push docker image
# -----------------------------------------------------------------------------
echo ">>> Building docker image: $IMAGE_NAME:$TAG"
docker build -t "$IMAGE_NAME:$TAG" .

echo ">>> Pushing docker image"
docker push "$IMAGE_NAME:$TAG"

# -----------------------------------------------------------------------------
# Git commit & push
# -----------------------------------------------------------------------------
echo ">>> Committing code to git"
git add .
git commit -m "Publish $TAG"
git push

echo ">>> Done. Published $IMAGE_NAME:$TAG"
