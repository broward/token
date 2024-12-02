from jschon import create_catalog, JSON, JSONSchema
from os import walk
from typing import Final
import json
import pathlib

create_catalog('2020-12')

SCHEMA_COUNT: Final = 8

schema = [''] * SCHEMA_COUNT
schema[0] = 'header'
schema[1] = 'address'
schema[2] = 'quorum_entry'
schema[3] = 'key'
schema[4] = 'key_request'
schema[5] = 'person'
schema[6] = 'transaction'
schema[7] = 'status'

#data_dir = pathlib.Path(__file__).parent / '../test'

# load all schemas
schema_dir = pathlib.Path(__file__).parent / './schema'
print(schema_dir)
validator = [] * SCHEMA_COUNT
for i in schema:
    s = str(i + '.json')
    print(s)
    validator.append(JSONSchema.loadf(schema_dir / s))

# data.append(JSON.loadf(data_dir / str(s)))



# Validate the JSON data
for i in range(7):
    result = validator[i].evaluate(data[i])

    print(schema[i] + ' returned: ' + str(result))
