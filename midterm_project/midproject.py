import json

def read_json(filename):
    with open(filename, 'r') as f,open('customers.json','w') as f1,open('items.json','w')as f2:
        reads= json.load(f)
        dict1={}
        dict2={}
        for item in range(len(reads)):
            dict1[reads[item]['phone']]=reads[item]['name']
            for item_name in reads[item]['items']:
                if item_name['name'] not in dict2:
                    dict2[item_name['name']]={}
                    dict2[item_name['name']]['price']=item_name['price']
                    dict2[item_name['name']]['orders']=1
                else:
                    dict2[item_name['name']]['orders'] += 1
        f1.write(json.dumps(dict1))
        f2.write(json.dumps(dict2))        

read_json('example_orders.json')