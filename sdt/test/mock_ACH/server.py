from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError

app = Flask(__name__)

# ACH Schema
ACH_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "transaction_id": {"type": "string"},
        "payer": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "account_number": {"type": "string"},
                "routing_number": {"type": "string", "pattern": "^[0-9]{9}$"}
            },
            "required": ["name", "account_number", "routing_number"]
        },
        "payee": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "account_number": {"type": "string"},
                "routing_number": {"type": "string", "pattern": "^[0-9]{9}$"}
            },
            "required": ["name", "account_number", "routing_number"]
        },
        "amount": {"type": "number", "minimum": 0},
        "currency": {"type": "string", "pattern": "^[A-Z]{3}$"},
        "transaction_date": {"type": "string", "format": "date-time"},
        "memo": {"type": "string"}
    },
    "required": ["transaction_id", "payer", "payee", "amount", "currency", "transaction_date"]
}

@app.route("/ach_transaction", methods=["POST"])
def ach_transaction():
    data = request.json
    try:
        validate(instance=data, schema=ACH_SCHEMA)
        # Validation passed, transaction is valid
        return jsonify({"success": True, "valid": True}), 200
    except ValidationError as e:
        # Validation failed
        return jsonify({"success": False, "error": e.message}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)

