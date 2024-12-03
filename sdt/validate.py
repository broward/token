from jsonschema import *
from pathlib import *
import json, os
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
path = Path(dir_path + '/schema')
filelist = []
for f in path.iterdir():
    filelist.append(f)

for file in filelist:
    with file.open() as schema_file:   
        sdt_schema = json.load(schema_file)

print(sdt_schema)

dir_path = os.path.dirname(os.path.realpath(__file__))
path = Path(dir_path + '/test')
filelist = []
for f in path.iterdir():
    filelist.append(f)

for file in filelist:
    with file.open() as test_file:   
        test = json.load(test_file)
        print(test)
        try:
            validate(instance=test, schema=sdt_schema)
        except ValidationError as ex:
            print('error:' + str(ex))