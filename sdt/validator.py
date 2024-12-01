from jschon import create_catalog, JSON, JSONSchema
import json

create_catalog('2020-12')

# Define the schema
with open('schema/key.json', 'r') as f:
    demo_schema = JSONSchema(json.load(f))

# Define the JSON data
with open('../test/key.json', 'r') as f:
    data = f.read()  

print(demo_schema)
print(data)

# Validate the JSON data
result = demo_schema.evaluate(JSON(data))

print("JSON data is valid.")

