#!/bin/bash

cat << "EOF"

__| |______________________________________________________________________| |__
__   ______________________________________________________________________   __
  | |                                                                      | |
  | |                                                                      | |
  | |   ____            _                      _                   _       | |
  | |  |  _ \  ___  ___(_) __ _ _ __   ___  __| |   __ _ _ __   __| |      | |
  | |  | | | |/ _ \/ __| |/ _` | '_ \ / _ \/ _` |  / _` | '_ \ / _` |      | |
  | |  | |_| |  __/\__ \ | (_| | | | |  __/ (_| | | (_| | | | | (_| |      | |
  | |  |____/ \___||___/_|\__, |_| |_|\___|\__,_|  \__,_|_| |_|\__,_|      | |
  | |                     |___/                                            | |
  | |   _____             _                              _   _             | |
  | |  | ____|_ __   __ _(_)_ __   ___  ___ _ __ ___  __| | | |__  _   _   | |
  | |  |  _| | '_ \ / _` | | '_ \ / _ \/ _ \ '__/ _ \/ _` | | '_ \| | | |  | |
  | |  | |___| | | | (_| | | | | |  __/  __/ | |  __/ (_| | | |_) | |_| |  | |
  | |  |_____|_| |_|\__, |_|_| |_|\___|\___|_|  \___|\__,_| |_.__/ \__, |  | |
  | |               |___/                                          |___/   | |
  | |   _  __    _     _ _   _  _                                          | |
  | |  | |/ /___| |__ (_) |_(_)(_)                                         | |
  | |  | ' // __| '_ \| | __| || |                                         | |
  | |  | . \\__ \ | | | | |_| || |                                         | |
  | |  |_|\_\___/_| |_|_|\__|_|/ |                                         | |
  | |                        |__/                                          | |
  | |                                                                      | |
__| |______________________________________________________________________| |__
__   ______________________________________________________________________   __
  | |                                                                      | |

EOF

# Declaring variables
line="=================================="

# Update and upgrade packages
echo -e "$line\nUpdating and upgrading packages.\n$line\n"
sudo apt update && sudo apt upgrade -y
echo -e "$line\nFinished updating and upgrading packages.\n$line\n"

# Check if python3-pip is installed
echo -e "$line\nChecking for python3-pip.\n$line\n"
if ! dpkg -l | grep -q python3-pip; then
  echo -e "$line\npython3-pip is not installed,\nInstalling python3-pip.\n$line\n"
  sudo apt install python3-pip -y
else
  echo -e "$line\npython3-pip already installed, moving on...\n$line\n"
fi

# Create project folder
USER=$(whoami)
PROJECT_DIR="/home/$USER/Desktop/dht11-sensor"

if [ ! -d "$PROJECT_DIR" ]; then
  echo -e "$line\nCreating 'dht11-sensor' in Desktop directory for current user.\n$line\n"
  mkdir -p "$PROJECT_DIR"
  cp "./temp-calc.py" "$PROJECT_DIR/"
  cp -r "./DHT11_Python/" "$PROJECT_DIR/DHT11_Python"
  echo -e "$line\nCreated '$PROJECT_DIR' directory.\n$line\n"
else
  echo -e "$line\n$PROJECT_DIR already exists.\n$line\n"
fi

# Create and activate Python virtual environment
cd "$PROJECT_DIR/"
chmod 775 ./temp-calc.py
python3 -m venv .
echo -e "$line\nVirtual environment created.\n$line\n"
echo -e "$line\nActivating virtual environment...\n$line\n"
source $PROJECT_DIR/bin/activate

echo -e "$line\nInstalling dependencies...\n$line\n"
pip install --upgrade RPi.GPIO setuptools
# Alternatively, instead of executing the next four lines, you can also run "pip install dht11"
# but I've decided to keep the files for "dht11" package locally available for installation in the script.
cd "$PROJECT_DIR/DHT11_Python"
pip install .
pip show dht11
cd "$PROJECT_DIR/"

echo -e "\n\n\n$line$line$line\nSetup completed.\nExecute the command 'python3 temp-calc.py' to calculate the temperature.\n# DESIGNED AND ENGINEERED BY KSHITIJ.\n# END OF SCRIPT\n$line$line$line\n\n\n"
