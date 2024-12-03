from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database (in-memory)
db = {
    "users": [],
    "addresses": [],
    "accounts": [],
    "transactions": []
}

@app.route("/user", methods=["POST"])
def create_user():
    user = request.json
    db["users"].append(user)
    return jsonify({"message": "User created", "user": user}), 201

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(db["users"])

@app.route("/account", methods=["POST"])
def create_account():
    account = request.json
    db["accounts"].append(account)
    return jsonify({"message": "Account created", "account": account}), 201

@app.route("/accounts", methods=["GET"])
def get_accounts():
    return jsonify(db["accounts"])

@app.route("/transaction", methods=["POST"])
def create_transaction():
    transaction = request.json
    db["transactions"].append(transaction)
    return jsonify({"message": "Transaction created", "transaction": transaction}), 201

@app.route("/transactions", methods=["GET"])
def get_transactions():
    return jsonify(db["transactions"])

if __name__ == "__main__":
    app.run(debug=True)
