# Use Python base image
FROM python:3.9-slim

# Set the working directory variable
ARG API_DIR

WORKDIR /app

# Copy only the necessary API files
COPY ${API_DIR}/server.py /app/server.py
COPY ${API_DIR}/schema.json /app/schema.json
# COPY schema/env.json /app/env.json
# COPY schema/sdt.json /app/sdt.json

# server
RUN pip3.9 install requests
RUN pip3.9 install DynaConf
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

# Command to start the server
CMD ["python", "server.py"]
