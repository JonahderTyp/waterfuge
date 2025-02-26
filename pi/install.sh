
# Exit immediately if a command exits with a non-zero status
set -e

# Inform the user about what the script does
echo "Setting up your environment..."

# Update package lists and install tmux
echo "Installing tmux..."
sudo apt-get update && sudo apt-get install tmux -y && sudo apt-get install python3-rpi.gpio -y

# Remove existing virtual environment if it exists
if [ -d ".venv" ]; then
    echo "Existing virtual environment detected. Removing it..."
    rm -rf .venv
fi

# Create a Python virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv .venv

# Activate the virtual environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source .venv/bin/activate
if [ -f "requirements.txt" ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
else
    echo "No requirements.txt found, skipping package installation."
fi
deactivate

# Copy config.example.cfg to config.cfg if it doesn't already exist
if [ -f "config.example.cfg" ]; then
    if [ ! -f "config.cfg" ]; then
        echo "Copying config.example.cfg to config.cfg..."
        cp config.example.cfg config.cfg
    else
        echo "config.cfg already exists. Skipping copy."
    fi
else
    echo "config.example.cfg not found. Skipping config copy."
fi

# Make the start script executable
echo "Making start.sh executable..."
chmod +x start.sh

# Add start script to crontab if not already present
CRON_JOB="@reboot /home/summer/waterfuge/pi/start.sh"
echo "Checking if crontab entry exists..."
(crontab -l 2>/dev/null | grep -qF "$CRON_JOB") || (
    echo "Adding start script to crontab for reboot..."
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
)

# Final message
echo "Setup completed successfully!"