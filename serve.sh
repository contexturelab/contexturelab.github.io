#!/bin/bash

# Local development server script for Contexture Lab website
# This script runs Jekyll without live-reload to avoid eventmachine dependency issues

echo "Starting Jekyll development server..."
echo "Site will be available at: http://localhost:4000"
echo ""
echo "Note: Auto-reload is disabled. Manually refresh your browser after making changes."
echo "Press Ctrl+C to stop the server."
echo ""

# Try to use bundle if gems are installed, otherwise use jekyll directly
if bundle exec jekyll --version &> /dev/null; then
    bundle exec jekyll serve --port 4000 --host 0.0.0.0 --livereload false --incremental
else
    echo "Bundle not available, trying jekyll directly..."
    jekyll serve --port 4000 --host 0.0.0.0 --livereload false --incremental
fi
