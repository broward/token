from jschon import create_catalog, JSON, JSONSchema, URI, LocalSource
from os import walk
from typing import Final
import json
import pathlib

catalog = create_catalog('2020-12')
schema_dir = pathlib.Path(__file__).parent / './schema'
data_dir = pathlib.Path(__file__).parent / './test'

catalog.add_uri_source(URI('https://example.com/'), LocalSource(schema_dir, suffix='.json'))
sdt_schema = catalog.get_schema(URI('https://example.com/sdt-schema'))

header = JSON.loadf(data_dir / 'header.json')
person = JSON.loadf(data_dir / 'person.json')
address = JSON.loadf(data_dir / 'address.json')
status = JSON.loadf(data_dir / 'status.json')

print("header test: " + str(sdt_schema.evaluate(header)))
print("person test: " + str(sdt_schema.evaluate(person)))
print("address test: " + str(sdt_schema.evaluate(address)))
print("status test: " + str(sdt_schema.evaluate(status)))

