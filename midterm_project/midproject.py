import json

def read_json(filename):
    with open(filename, 'r') as f:
        reads= json.load(f)
        customer={}
        items={}
        for item in range(len(reads)):
            customer[reads[item]['phone']]=reads[item]['name']
            for item_name in reads[item]['items']:
                if item_name['name'] not in items:
                    items[item_name['name']]={}
                    items[item_name['name']]['price']=item_name['price']
                    items[item_name['name']]['orders']=1
                else:
                    items[item_name['name']]['orders'] += 1
    with open('customers.json','w') as f1:
        f1.write(json.dumps(customer))
    with open('items.json','w') as f2:
        f2.write(json.dumps(items))        

read_json('example_orders.json')
