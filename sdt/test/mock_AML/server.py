from flask import Flask, request, jsonify
from jsonschema import validate, ValidationError

app = Flask(__name__)

# AML Schema
AML_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "customer_id": {"type": "string"},
        "transaction_id": {"type": "string"},
        "amount": {"type": "number", "minimum": 0},
        "currency": {"type": "string", "pattern": "^[A-Z]{3}$"},
        "transaction_date": {"type": "string", "format": "date-time"},
        "source_of_funds": {"type": "string"},
        "destination_of_funds": {"type": "string"},
        "risk_level": {"type": "string", "enum": ["low", "medium", "high"]},
        "compliance_check": {"type": "boolean"}
    },
    "required": [
        "customer_id",
        "transaction_id",
        "amount",
        "currency",
        "transaction_date",
        "source_of_funds",
        "destination_of_funds",
        "risk_level",
        "compliance_check"
    ]
}

@app.route("/aml_check", methods=["POST"])
def aml_check():
    data = request.json
    try:
        validate(instance=data, schema=AML_SCHEMA)
        # If compliance_check is true and risk_level is "low" or "medium", return True
        compliance = data["compliance_check"] and data["risk_level"] in ["low", "medium"]
        return jsonify({"success": True, "compliance": compliance}), 200
    except ValidationError as e:
        return jsonify({"success": False, "error": e.message}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
