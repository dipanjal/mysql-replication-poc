#!/bin/bash

echo "Cleaning up FastAPI application..."

# Remove virtual environment
if [ -d ".venv" ]; then
    echo "Removing virtual environment..."
    rm -rf .venv
fi

# Remove Python cache files
echo "Removing Python cache files..."
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete
find . -type d -name "*.pyo" -delete
find . -type d -name "*.pyd" -delete

# Remove pytest cache
if [ -d ".pytest_cache" ]; then
    echo "Removing pytest cache..."
    rm -rf .pytest_cache
fi

# Remove mypy cache
if [ -d ".mypy_cache" ]; then
    echo "Removing mypy cache..."
    rm -rf .mypy_cache
fi

# Remove coverage files
echo "Removing coverage files..."
find . -name "*.cover" -delete
find . -name ".coverage*" -delete

# Remove log files
echo "Removing log files..."
find . -name "*.log" -delete

# Remove temporary files
echo "Removing temporary files..."
find . -name "*.tmp" -delete
find . -name "*.temp" -delete

echo "Cleanup completed!"
