from config_loader import ConfigLoader
from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError
import boto3
import json

# Load configurations from env.json and sdt.json
settings = ConfigLoader()
print("aml:", settings.get("aml_server"))
print("secrets:", settings.get("secrets_store").get("access_key"))

SCHEMA="schema.json"
AWS_DEFAULT_REGION="us-east-1"

# Load configurations from env.json and sdt.json
settings = ConfigLoader()

# Load the JSON schemas
with open(SCHEMA) as f:
    sdt_schema = json.load(f)

# Flask application
app = Flask(__name__)

# AWS SQS Client
sqs_client = boto3.client(
    "sqs",
    aws_access_key_id=settings.get("secrets_store").get("access_key"),
    aws_secret_access_key="YOUR_SECRET_KEY",  # Replace with actual secret key
    region_name=AWS_DEFAULT_REGION  # Replace with the appropriate AWS region
)

# Helper method to validate JSON with schema
def validate_message(message, schema):
    try:
        validate(instance=message, schema=schema)
        return True, None
    except ValidationError as e:
        return False, str(e)

# Method: send_to_mcp
def send_to_mcp(transaction_message):
    # Simulate sending the transaction to an MCP object
    print(f"Sending to MCP: {transaction_message}")
    return {"status": "sent", "target": "MCP"}

# Method: write_to_sqs
def write_to_sqs(transaction_message):
    try:
        queue_url = settings.sqs_queue  # Get queue URL from the configuration
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(transaction_message)
        )
        return {"status": "success", "message_id": response["MessageId"]}
    except Exception as e:
        return {"status": "error", "error": str(e)}

# Method: read_from_sqs
def read_from_sqs(transaction_id):
    try:
        queue_url = settings.sqs_queue  # Get queue URL from the configuration
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1
        )
        if "Messages" in response:
            for message in response["Messages"]:
                body = json.loads(message["Body"])
                if body.get("transaction_id") == transaction_id:
                    return {"status": "found", "message": body}
        return {"status": "not_found"}
    except Exception as e:
        return {"status": "error", "error": str(e)}

# REST API: Send user JSON to a variable URL
@app.route("/register_user", methods=["POST"])
def register_user():
    data = request.json
    url = request.args.get("url")  # Accept variable URL from query parameters
    # Here, we could send the data to the specified URL (e.g., using requests library)
    print(f"Registering user JSON to {url}: {data}")
    return jsonify({"status": "sent", "url": url, "data": data})

# REST API: Get tracking ID
@app.route("/get_tracking_id", methods=["GET"])
def get_tracking_id():
    tracking_id_json = {
        "message_type": "tracking_id",
        "tracking_id": 123456  # Example tracking ID
    }
    return jsonify(tracking_id_json)

# REST API: Run transaction
@app.route("/run_transaction", methods=["POST"])
def run_transaction():
    transaction_message = request.json
    is_valid, error = validate_message(transaction_message, sdt_schema)
    if not is_valid:
        return jsonify({"error": error}), 400

    transaction_id = transaction_message["payload"]["transaction_id"]
    print("transaction id validated:" + str(transaction_id))
    print("queuing transaction to sqs")
    sqs_response = write_to_sqs(transaction_message)
    
    print("reading from sqs")
    queue_entry = read_from_sqs(transaction_id)
    
    # Example: Send the transaction to MCP and SQS
    mcp_response = send_to_mcp(queue_entry)
    print("mcp_response:" + str(mcp_response))
    
    return jsonify({"mcp_response": mcp_response, "sqs_response": sqs_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


