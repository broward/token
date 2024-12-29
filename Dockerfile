# Use Python base image
FROM python:3.9-slim

RUN apt-get update && apt-get install -y awscli

RUN pip install --upgrade pip
RUN pip install awscli-local

RUN pip install --upgrade setuptools

# Set the working directory variable
ARG API_DIR
ARG CONFIG_DIR

WORKDIR /app

# Copy only the necessary API files
COPY ${API_DIR}/*.*  /app
# COPY ${API_DIR}/server.py /app/server.py
COPY ${API_DIR}/schema.json /app/schema.json
COPY ${CONFIG_DIR}/env.json /app/env.json


# server
RUN pip3.9 install requests
RUN pip3.9 install boto3

# database
RUN pip3.9 install flask
RUN pip3.9 install jsonify
RUN pip3.9 install peewee
RUN pip3.9 install psycopg2-binary

# Update jsonschema
RUN pip3.9 install --upgrade jsonschema

# Expose the appropriate port dynamically
ARG PORT
EXPOSE ${PORT}

#RUN chmod -R 755 /usr/local/aws-cli/
RUN export PATH=/usr/local/bin:$PATH
# RUN source ~/.bash_profile

# Command to start the server
CMD ["python", "server.py"]
