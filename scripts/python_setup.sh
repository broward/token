
sudo apt install python3.9-distutils

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


