# client.py
import json
import requests
import pprint
from config_loader import ConfigLoader

# Create a sample user
user = {
  "message_type": "user",
  "payload": {
    "header": {
      "message_type": "user",
      "version": 1.0,
      "tracking_id": 12345,
      "create_date": "2024-12-28"
    },
    "user_id": 101,
    "first_name": "John",
    "last_name": "Doe",
    "address": {
      "header": {
        "message_type": "address",
        "version": 1.0,
        "tracking_id": 67890,
        "create_date": "2024-12-28"
      },
      "address_1": "123 Main St",
      "address_2": "Apt 4B",
      "city": "Springfield",
      "state": "IL",
      "zipcode": "62704",
      "update_date": "2024-12-28"
    },
    "email": "john.doe@example.com",
    "password": "securepassword123",
    "phone": "+1234567890",
    "time_zone": "CST",
    "update_date": "2024-12-28"
  }
}


# Create a transaction JSON
transaction = {
    "message_type": "transaction",
    "payload": {
        "header": {
            "message_type": "transaction",
            "version": 1.0,
            "tracking_id": 0,
            "create_date": "2024-12-13"
        },
        "depo_type": "gold",
        "transaction_id": 1001,
        "payer": 100,
        "payee": 200,
        "amount": 500.0
    }
}

settings = ConfigLoader()

# get SDT server url
sdt_url = settings.get(ConfigLoader.SDT_SERVER)
print("sdt_url=" + sdt_url)

def get_tracking_id(base_url=sdt_url, endpoint="/get_tracking_id"):

    url = f"{base_url}{endpoint}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return the parsed JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")
        return None
    
def run_transaction(base_url=sdt_url, endpoint="/run_transaction", payload=None):

    url = f"{base_url}{endpoint}"
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        return response.json()  # Return the parsed JSON response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")
        return None


if __name__ == "__main__":
    # register a user

    # Get tracking id
    tracking_id_response = get_tracking_id()

    if tracking_id_response:
        print("Tracking ID Response:", tracking_id_response)
        transaction["payload"]["header"]["tracking_id"] = tracking_id_response["tracking_id"]
        print("Transaction:", transaction)
    else:
        print("Failed to retrieve tracking ID.")

    transaction_response = run_transaction(payload=transaction)

    if transaction_response:
        print("Transaction Response:", transaction_response)
    else:
        print("Failed to send transaction.")





