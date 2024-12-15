# client.py
import requests
import json
from dynaconf import Dynaconf

# Load configuration
settings = Dynaconf(settings_files=["env.json"])

# Create a transaction JSON
transaction = {
    "message_type": "transaction",
    "payload": {
        "header": {
            "message_type": "transaction",
            "version": 1.0,
            "tracking_id": 12345,
            "create_date": "2024-12-13"
        },
        "depo_type": "gold",
        "transaction_id": 1001,
        "payer": 100,
        "payee": 200,
        "amount": 500.0
    }
}

# REST API to send JSON
response = requests.post("http://localhost:5000/api/validate", json=transaction)
print("Response:", response.json())

