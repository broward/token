sudo apt install curl

# install pinta
sudo apt update
sudo apt install snapd
sudo snap install pinta

# install libreoffice
sudo apt update
sudo apt update && sudo apt upgrade -y
sudo snap install libreoffice

# install nodejs to support Quorum quickstart
sudo apt update
sudo apt install nodejs

# java

# DBVisualizer
/master/Installs/

# ssh
ssh-keygen

# git
sudo apt install git
git config --global user.email "browardhorne@gmail.com"
git config --global user.name "Broward Horne"

# browsers
sudo apt update
sudo snap install brave
sudo apt update
sudo apt install opera

sudo apt install keepassxc

sudo apt update
sudo apt install software-properties-common curl apt-transport-https ca-certificates -y
sudo apt remove docker-desktop
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-archive-keyring.gpg
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt install docker-ce docker-ce-cli containerd.io uidmap -y
sudo systemctl status docker

# docker desktop
wget https://desktop.docker.com/linux/main/amd64/docker-desktop-4.19.0-amd64.deb
sudo apt install ./docker-desktop-*-amd64.deb

# docker desktop crashes
# sudo nano /etc/sysctl.conf
# add kernel.apparmor_restrict_unprivileged_userns=0
# sudo sysctl -p

# scrcpy
# runtime dependencies
sudo apt install ffmpeg libsdl2-2.0-0 adb libusb-1.0-0

# client build dependencies
sudo apt install gcc git pkg-config meson ninja-build libsdl2-dev \
                 libavcodec-dev libavdevice-dev libavformat-dev libavutil-dev \
                 libswresample-dev libusb-1.0-0-dev
                 # runtime dependencies

sudo apt update
sudo snap install scrcpy
sudo apt-get install gnome-search-tool

sudo apt update
sudo apt install pulseaudio pulseaudio-module-bluetooth gstreamer1.0-pulseaudio pulseaudio-utils
sudo apt install pavucontrol

systemctl --user stop pipewire.socket pipewire-pulse.socket
systemctl --user disable pipewire.socket pipewire-pulse.socket
systemctl --user mask pipewire.socket pipewire-pulse.socket
systemctl --user enable pulseaudio.service pulseaudio.socket
systemctl --user start pulseaudio.service pulseaudio.socket





