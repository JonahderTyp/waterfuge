#!/bin/bash

SESSION_NAME="waterfuge"
WINDOW_NAME="window"
PROJECT_DIR="/home/summer/waterfuge/pi"

# Start a new tmux session or attach to an existing one
tmux new-session -d -s $SESSION_NAME

# Send commands to the tmux session
tmux send-keys -t $SESSION_NAME "cd $PROJECT_DIR" C-m
tmux send-keys -t $SESSION_NAME ". .venv/bin/activate" C-m
tmux send-keys -t $SESSION_NAME "python -m datasender" C-m
