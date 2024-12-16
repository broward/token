# create our python environment
# remove existing environment
rm -r -f sdt_venv

# Script to create a Python virtual environment
sudo apt install python3.9-venv

# Set the virtual environment name
VENV_NAME="sdt_venv"

# Create the virtual environment
python3.9 -m venv "$VENV_NAME"

source sdt_venv/bin/activate

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
#python3.9 -m venv ~/py_envs
#source ~/py_envs/bin/activate

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py

# server
pip install requests
pip install dynaconf
pip install fastapi
pip install pynacl
pip install boto3
pip install pydantic

# database
pip install flask
pip install jsonify
pip install peewee
pip install psycopg2-binary

# https://python-jsonschema.readthedocs.io/en/stable/
pip install --upgrade jsonschema

# MPC library
git clone https://github.com/lschoe/mpyc.git
pip install ./mpyc --ignore-requires-python --target .

# integration testing, fix pip first
pip install setuptools --upgrade
# pip install localstack - now in docker-compose.
pip install awscli
#aws --endpoint-url=http://localhost:4566

aws configure
# export AWS_ACCESS_KEY_ID="test"
# export AWS_SECRET_ACCESS_KEY="test"
# export AWS_DEFAULT_REGION="us-east-1"


# alternate validator https://github.com/marksparkza/jschon
# pip install jschon
# pip install jschon[requests]


