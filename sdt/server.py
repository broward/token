import os
import uuid
import json
from fastapi import FastAPI, HTTPException
from dynaconf import Dynaconf
from pydantic import BaseModel
from nacl.signing import VerifyKey
import boto3
import requests

# Load Dynaconf settings based on environment variable
env = os.getenv("ENV_FOR_DYNACONF", "prod")
settings = Dynaconf(
    settings_files=["settings.json"],
    environments=True,
    env=env
)

# Initialize FastAPI
app = FastAPI()

# AWS SQS client
sqs_client = boto3.client("sqs", region_name="us-east-1")

# Base model for signed messages
class SignedMessage(BaseModel):
    message: str
    signature: str
    public_key: str


@app.get("/get_tracking_id")
def get_tracking_id():
    """
    Generates and returns a unique GUID value.
    """
    return {"tracking_id": str(uuid.uuid4())}


@app.post("/run_transaction")
def run_transaction(data: SignedMessage):
    """
    Accepts a signed EDDSA JSON message, unsigns it, and returns a result boolean.
    """
    try:
        public_key = VerifyKey(bytes.fromhex(data.public_key))
        message_bytes = data.message.encode()
        signature_bytes = bytes.fromhex(data.signature)
        public_key.verify(message_bytes, signature_bytes)

        message_json = json.loads(data.message)
        return {"result": True, "message": message_json}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid signature or message: {str(e)}")


def _read_from_sqs():
    """
    Private method to read a JSON message from SQS.
    """
    try:
        response = sqs_client.receive_message(
            QueueUrl=settings.sqs_queue,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=5,
        )
        messages = response.get("Messages", [])
        if not messages:
            return None
        message = messages[0]
        receipt_handle = message["ReceiptHandle"]
        sqs_client.delete_message(QueueUrl=settings.sqs_queue, ReceiptHandle=receipt_handle)
        return json.loads(message["Body"])
    except Exception as e:
        raise RuntimeError(f"Failed to read from SQS: {str(e)}")


def _write_to_sqs(message):
    """
    Private method to write a JSON message to SQS.
    """
    try:
        sqs_client.send_message(
            QueueUrl=settings.sqs_queue,
            MessageBody=json.dumps(message),
        )
    except Exception as e:
        raise RuntimeError(f"Failed to write to SQS: {str(e)}")


@app.post("/send_to_mcp")
def send_to_mcp(message: dict):
    """
    Sends a JSON message to MCP library.
    """
    try:
        mcp_url = settings.external_auth + "/mcp"
        response = requests.post(fireblocks_url, json=message)
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send to MCP: {str(e)}")

