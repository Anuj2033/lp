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

# Check if libgpiod2 is installed
echo -e "$line\nChecking for libgpiod2.\n$line\n"
if ! dpkg -l | grep -q libgpiod2; then
  echo -e "$line\nlibgpiod2 is not installed,\nInstalling python3-setuptools.\n$line\n"
  sudo apt install libgpiod2 -y
else
  echo -e "$line\nlibgpiod2 already installed, moving on...\n$line\n"
fi

# Create project folder
USER=$(whoami)
PROJECT_DIR="/home/$USER/Desktop/temp-sensor"

if [ ! -d "$PROJECT_DIR" ]; then
  echo -e "$line\nCreating 'temp-sensor' in Desktop directory for current user.\n$line\n"
  mkdir -p "$PROJECT_DIR"
  cp "./alt-temp.py" "./blinka-test.py" "$PROJECT_DIR/"
  echo -e "$line\nCreated '$PROJECT_DIR' directory.\n$line\n"
else
  echo -e "$line\n$PROJECT_DIR already exists.\n$line\n"
fi

# Create and activate Python virtual environment
cd "$PROJECT_DIR/"
chmod 775 ./alt-temp.py ./blinka-test.py
python3 -m venv . --system-site-packages
echo -e "$line\nVirtual environment created.\n$line\n"
echo -e "$line\nActivating virtual environment...\n$line\n"
source $PROJECT_DIR/bin/activate

echo -e "$line\nInstalling dependencies...\n$line\n"
pip3 install --upgrade setuptools click adafruit-python-shell adafruit-circuitpython-dht RPi.GPIO adafruit-blinka board

echo -e "$line\nSetting up raspiberry pi...\n$line\n"
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_spi 0
sudo raspi-config nonint do_serial_hw 0
sudo raspi-config nonint do_ssh 0
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint disable_raspi_config_at_boot 0
sudo apt install -y i2c-tools libgpiod-dev python3-libgpiod

python3 blinka-test.py
echo -e "$line\nBlinka works!\n$line\n"

echo -e "\n\n\n$line$line$line\nSetup completed.\nExecute the command 'python3 alt-temp.py' to calculate the temperature.\n# DESIGNED AND ENGINEERED BY KSHITIJ.\n# END OF SCRIPT\n$line$line$line\n\n\n"
