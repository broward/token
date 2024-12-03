 https://desktop.docker.com/linux/main/amd64/docker-desktop-amd64.deb
 
 sudo apt install gnome-terminal
 sudo apt-get update
 chmod u+x ./docker-desktop-amd64.deb
 sudo apt-get install ./docker-desktop-amd64.deb
 systemctl --user start docker-desktop
 systemctl --user enable docker-desktop
 systemctl --user stop docker-desktop
