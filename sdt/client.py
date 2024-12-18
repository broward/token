# client.py
import json
import pprint
from config_loader import ConfigLoader

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

# if __name__ == "__main__":
    # Load 'test' environment
config = ConfigLoader(environment=None)
print("DEBUG:", config.get("DEBUG"))
print("DATABASE_URL:", config.get("DATABASE_URL"))
print("API_KEY:", config.get("API_KEY"))




