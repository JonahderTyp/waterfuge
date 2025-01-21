
# Exit immediately if a command exits with a non-zero status
set -e

# Inform the user about what the script does
echo "Setting up your environment..."

# Update package lists and install tmux
echo "Installing tmux..."
sudo apt-get update && sudo apt-get install tmux -y

# Create a Python virtual environment
echo "Creating a Python virtual environment..."
python3 -m venv .venv

# Make the start script executable
echo "Making start.sh executable..."
chmod +x start.sh

# Setup crontab for running the script at reboot
echo "Adding start script to crontab for reboot..."
(crontab -l 2>/dev/null; echo "@reboot /home/summer/waterfuge/pi/start.sh") | crontab -

# Final message
echo "Setup completed successfully!"