sudo apt install curl

# install pinta
sudo apt update
sudo apt install snapd
sudo snap install pinta

# install libreoffice
sudo apt update
sudo apt update && sudo apt upgrade -y
sudo snap install libreoffice

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

sudo apt update
sudo apt install pulseaudio pulseaudio-module-bluetooth pulseaudio-utils
sudo apt install pavucontrol
systemctl --user mask pipewire.service pipewire.socket wireplumber.service wireplumber@.service pipewire-pulse.service pipewire-pulse.socket


sudo apt install flatpak
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

flatpak install flathub com.github.taiko2k.tauonmbflatpak run org.kde.elisa
flatpak run com.github.taiko2k.tauonmb





