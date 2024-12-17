# client.py
import json
from std_config import SDTConfig

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

def __init__(self):
    env = SDTConfig()
    #self.config = STDConfig("env.json")
    #self.base_url = self.config.get_value("api_base_url")



