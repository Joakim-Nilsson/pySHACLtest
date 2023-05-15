# -*- coding: utf-8 -*-
from pyshacl import validate
from os import path
import json

shacl_file = \
    filepath = "path/to/your/shape/file.ttl"

data_graph = \
    filepath = "C:\\Users\\joanilss\\FK\\instantiated_data.ttl"

shacl_file = path.abspath(shacl_file)
data_graph = path.abspath(data_graph)

# Run the validation
conforms, v_graph, v_text = validate(data_graph, shacl_graph=shacl_file, ont_graph=None, inference='none', abort_on_error=False, meta_shacl=False, debug=False, js=False, advanced=False)

result_json = json.dumps({
    "conforms": conforms,
    "validation_graph":v_graph,
    "validation_text": v_text
}, indent=4)

if conforms:
    print("Data conforms to SHACL shapes")
else:
    print(v_text)

print(json.dumps(result_json, indent=4))
print(result_json)

print(conforms)
print(v_graph)
print(v_text)
