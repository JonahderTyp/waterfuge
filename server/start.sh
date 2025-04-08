#!/bin/bash

SESSION_NAME="waterfuge"
WINDOW_NAME="window"
PROJECT_DIR="/home/summer/waterfuge/server"

# Start a new tmux session or attach to an existing one
tmux new-session -d -s $SESSION_NAME

# Send commands to the tmux session
tmux send-keys -t $SESSION_NAME "cd $PROJECT_DIR" C-m
tmux send-keys -t $SESSION_NAME ". .venv/bin/activate" C-m
tmux send-keys -t $SESSION_NAME "flask --app waterfuge:create_app run --host 0.0.0.0 -p 8080" C-m