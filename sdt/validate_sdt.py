from jschon import create_catalog, JSON, JSONSchema, URI, LocalSource
from os import walk
from typing import Final
import json
import pathlib

catalog = create_catalog('2020-12')
schema_dir = pathlib.Path(__file__).parent / './schema'
data_dir = pathlib.Path(__file__).parent / './test'

catalog.add_uri_source(URI('https://example.com/'), LocalSource(schema_dir, suffix='.json'))

# catalog.add_schema(URI('https://example.com/header'), 'header')
# sdt_schema = catalog.get_schema(URI('https://example.com/sdt'))
org_data = JSON.loadf(data_dir / 'header.json')
org_schema = catalog.get_schema(URI('https://example.com/sdt-schema'))

print(org_data)
result = org_schema.evaluate(org_data)
print(result.__dict__)
print(result.output('flag'))