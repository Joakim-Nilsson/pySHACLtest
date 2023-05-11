# -*- coding: utf-8 -*-
from pyshacl import validate
from os import path
import json

data_ttl_file = \
    filepath = "C:\\Users\\joanilss\\FK\\instantiated_data.ttl"


data_ttl_file = path.abspath(data_ttl_file) 


conforms, v_graph, v_text = validate(data_ttl_file, shacl_graph=None, inference='rdfs',
                                     serialize_report_graph=True)

result_json = json.dumps({
    "conforms": conforms,
    "validation_graph":v_graph.decode('utf-8'),
    "validation_text": v_text
}, indent=4)

print(json.dumps(result_json, indent=4))
print(result_json)

print(conforms)
print(v_graph)
print(v_text)
