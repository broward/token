from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Dummy URL for external services (replace with real ones)
KYB_API_URL = "http://example.com/kyc"
AML_API_URL = "http://example.com/aml"
ACH_API_URL = "http://example.com/ach"
BLOCKCHAIN_API_URL = "http://example.com/quorum"

# Dummy login check (replace with actual user validation)
USERS = {
    'user1': 'password123',
    'user2': 'password456'
}

# Function to handle external calls
def send_to_external_api(url, data):
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to contact {url}"}
    except Exception as e:
        return {"error": str(e)}

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in USERS and USERS[username] == password:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Transaction endpoint
@app.route('/transaction', methods=['POST'])
def transaction():
    data = request.get_json()

    # Assuming the transaction includes KYC, AML, ACH and Blockchain data
    kyc_data = data.get('kyc_data')
    aml_data = data.get('aml_data')
    ach_data = data.get('ach_data')
    blockchain_data = data.get('blockchain_data')

    # Sending data to external services
    kyc_response = send_to_external_api(KYB_API_URL, kyc_data)
    aml_response = send_to_external_api(AML_API_URL, aml_data)
    ach_response = send_to_external_api(ACH_API_URL, ach_data)
    blockchain_response = send_to_external_api(BLOCKCHAIN_API_URL, blockchain_data)

    # Returning responses from external services
    return jsonify({
        "kyc_response": kyc_response,
        "aml_response": aml_response,
        "ach_response": ach_response,
        "blockchain_response": blockchain_response
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
