sudo usermod -a -G docker $USER
sudo chmod 777 /var/run/docker.sock
sudo docker-compose up --build
