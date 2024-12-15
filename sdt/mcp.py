import requests
import json

def retrieve_key_shards():
    """
    Retrieves key shards from external sources and assembles them into a key.
    """
    external_auth_url = "http://localhost:500/external_auth"
    client_url = "http://localhost:500/client"
    rds_database_url = "http://localhost:500/rds"

    shard1 = requests.get(external_auth_url + "/key_shard").json()["shard"]
    shard2 = requests.get(client_url + "/key_shard").json()["shard"]
    shard3 = requests.get(rds_database_url + "/key_shard").json()["shard"]

    # Assemble shards into a key (mocked here)
    key = shard1 + shard2 + shard3
    return key


def execute_transaction(key, transaction_data):
    """
    Executes a transaction using the assembled key and writes to Quorum blockchain.
    """
    try:
        # Use the key to sign the transaction (mocked signing)
        signed_transaction = {"key": key, "transaction_data": transaction_data}

        # Write to Quorum blockchain
        quorum_url = "http://localhost:500/quorum_chain"
        response = requests.post(quorum_url + "/write", json=signed_transaction)
        response.raise_for_status()

        return {"result": True}
    except Exception as e:
        return {"result": False, "error": str(e)}


def mcp_transaction(transaction_data):
    """
    Main MCP transaction process.
    """
    key = retrieve_key_shards()
    result = execute_transaction(key, transaction_data)
    return result

