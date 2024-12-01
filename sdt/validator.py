from jsonschema import validate, ValidationError 
# Define the schema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "serverName": {"type": "string"},
        "port": {"type": "integer", "minimum": 1, "maximum": 65535},
        "enabled": {"type": "boolean"}
    },
    "required": ["serverName", "port"]
}
# Define the JSON data
data = {
    "serverName": "MyServer",
    "port": 8080,
    "enabled": True
}
# Validate the JSON data
try:
    validate(instance=data, schema=schema)
    print("JSON data is valid.")
except ValidationError as e:
    print(f"JSON data is invalid: {e.message}")