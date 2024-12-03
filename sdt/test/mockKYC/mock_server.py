from flask import Flask, request, jsonify

app = Flask(__name__)

# JSON Schema for validation
KYC_SCHEMA = {
    "type": "object",
    "properties": {
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
        "date_of_birth": {"type": "string", "format": "date"},
        "nationality": {"type": "string"},
        "id_type": {"type": "string", "enum": ["passport", "driver_license", "national_id"]},
        "id_number": {"type": "string"},
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "city": {"type": "string"},
                "state": {"type": "string"},
                "zip_code": {"type": "string"},
                "country": {"type": "string"}
            },
            "required": ["street", "city", "state", "zip_code", "country"]
        },
        "email": {"type": "string", "format": "email"},
        "phone": {"type": "string"},
        "kyc_date": {"type": "string", "format": "date-time"}
    },
    "required": [
        "first_name",
        "last_name",
        "date_of_birth",
        "nationality",
        "id_type",
        "id_number",
        "address",
        "email",
        "phone",
        "kyc_date"
    ]
}

# Endpoint to receive KYC information
@app.route("/submit_kyc", methods=["POST"])
def submit_kyc():
    data = request.json

    # Validate JSON payload against schema
    from jsonschema import validate, ValidationError

    try:
        validate(instance=data, schema=KYC_SCHEMA)
        return jsonify({"success": True}), 200
    except ValidationError as e:
        return jsonify({"success": False, "error": e.message}), 400


if __name__ == "__main__":
    app.run(debug=True)
