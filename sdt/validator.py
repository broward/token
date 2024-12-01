from jschon import create_catalog, JSON, JSONSchema
import json
import pathlib

create_catalog('2020-12')

data_dir = pathlib.Path(__file__).parent / './schema'

common_schema = JSONSchema.loadf(data_dir / 'common.json')
address_schema = JSONSchema.loadf(data_dir / 'address.json')
person_schema = JSONSchema.loadf(data_dir / 'person.json')


print(common_schema)
print(person_schema)

# Validate the JSON data

print("JSON data is valid.")

