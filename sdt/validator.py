from jschon import create_catalog, JSON, JSONSchema
import json
import pathlib

create_catalog('2020-12')

schema = [''] * 7
schema[0] = 'common'
schema[1] = 'address'
schema[2] = 'chainEntry'
schema[3] = 'key'
schema[4] = 'keyRequest'
schema[5] = 'person'
schema[6] = 'transaction'

schema_dir = pathlib.Path(__file__).parent / './schema'
data_dir = pathlib.Path(__file__).parent / '../test'

validator = [] * 7
data = [] * 7
for i in schema:
    s = str(i + '.json')
    validator.append(JSONSchema.loadf(schema_dir / s))
    data.append(JSON.loadf(data_dir / str(s)))

# Validate the JSON data
for i in range(7):
    result = validator[i].evaluate(data[i])

    print(schema[i] + ' returned: ' + str(result))
