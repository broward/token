#!/bin/bash

# Set variables
SECRET_NAME="postgres-login"
SECRET_DESCRIPTION="PostgreSQL login credentials"
DB_USERNAME="postgres"
DB_PASSWORD="docker"
DB_HOST="localhost"
DB_PORT="5432" # Default PostgreSQL port
DB_NAME="postgres"
LOCALSTACK_ENDPOINT="http://localhost:4566" # Default LocalStack endpoint

# Create the JSON secret string
SECRET_STRING=$(cat <<EOF
{
  "username": "${DB_USERNAME}",
  "password": "${DB_PASSWORD}",
  "host": "${DB_HOST}",
  "port": "${DB_PORT}",
  "dbname": "${DB_NAME}"
}
EOF
)

# Create the secret in LocalStack's Secrets Manager
aws secretsmanager create-secret \
  --endpoint-url ${LOCALSTACK_ENDPOINT} \
  --name ${SECRET_NAME} \
  --description "${SECRET_DESCRIPTION}" \
  --secret-string "${SECRET_STRING}" \
  --region us-east-1

# Output success message
if [ $? -eq 0 ]; then
  echo "Secret '${SECRET_NAME}' successfully created in LocalStack Secrets Manager."
else
  echo "Failed to create the secret '${SECRET_NAME}'."
fi

