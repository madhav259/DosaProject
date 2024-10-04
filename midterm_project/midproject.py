import json

def read_json(filename):
    with open(filename, 'r') as f:
        reads= json.load(f)        

read_json('example_orders.json')