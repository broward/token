# client.py
import json
from sdt_config import *

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

def main():
    print("hello world")
    env = SDTConfig()
    host = env.get_value(env.AML_SERVER)
    print("my key value is " + host)
    #self.config = STDConfig("env.json")
    #self.base_url = self.config.get_value("api_base_url")

if __name__ == "__main__":
    main()


