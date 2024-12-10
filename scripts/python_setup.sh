# Install Python 3.9 and dependencies
sudo apt update
sudo apt install software-properties-common

# Add the deadsnakes PPA to your system’s sources list:
sudo apt install python3.9-distutils
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
sudo apt install python3-pip
python3.9 --version

# create venv
python3.9 -m venv ~/py_envs
source ~/py_envs/bin/activate

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
python3.9 get-pip.py --user

# server
pip install requests
pip install dynaconf
pip install fastapi
pip install nacl.signing
pip install boto3

# database
pip install flask
pip install jsonify
pip install peewee
pip install psycopg2-binary



# https://python-jsonschema.readthedocs.io/en/stable/
pip install --upgrade jsonschema

# alternate validator https://github.com/marksparkza/jschon
# pip install jschon
# pip install jschon[requests]


