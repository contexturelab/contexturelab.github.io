#!/bin/bash

# Docker-based Jekyll development server
# This is the most reliable method that avoids all Ruby dependency issues

echo "Starting Jekyll development server using Docker..."
echo "Site will be available at: http://localhost:4000"
echo ""
echo "Note: First run will take a few minutes to download the Docker image."
echo "Press Ctrl+C to stop the server."
echo ""

docker run --rm \
  --volume="$PWD:/srv/jekyll:Z" \
  --publish 4000:4000 \
  jekyll/jekyll:4 \
  jekyll serve --watch --force_polling --livereload
