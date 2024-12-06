
sudo apt install python3.9-distutils

# Install Python 3.9 and dependencies
sudo apt update
sudo apt install software-properties-common

Add the deadsnakes PPA to your system’s sources list:
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
python3.9 --version

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
python3.9 get-pip.py --user

# server
pip3.9 install requests

# database
pip3.9 install flask
pip3.9 install jsonify
pip3.9 install peewee
pip3.9 install psycopg2-binary

# https://python-jsonschema.readthedocs.io/en/stable/
pip3.9 install --upgrade jsonschema

# alternate validator https://github.com/marksparkza/jschon
pip3.9 install jschon
pip3.9 install jschon[requests]


