#!/bin/bash

# Add local environment variables from container-local.env
local_env_file="./env/local.env"

if [ -f "$local_env_file" ]; then
    # read .env file line by line
    while IFS= read -r line; do
        export "$line" # set environment variables from .env file
    done < "$local_env_file"
else
    echo "Error: $local_env_file does not exist."
fi


source .venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
