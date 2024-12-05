from fireblocks_sdk import FireblocksSDK

api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

fireblocks = FireblocksSDK(api_key, api_secret)

# Get vault accounts
vault_accounts = fireblocks.get_vault_accounts()
print(vault_accounts)

# Create a new transaction
transaction = fireblocks.create_transaction(
    asset_id="BTC",
    source={"type": "VAULT_ACCOUNT", "id": "YOUR_VAULT_ACCOUNT_ID"},
    destination={"type": "EXTERNAL_WALLET", "address": "YOUR_DESTINATION_ADDRESS"},
    amount=0.01
)
print(transaction)