import yaml

DATA_IN = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_ptice': {'computer': '800\u20ac-1000\u20ac',
                           'printer': '1000\u20ac-1500\u20ac',
                           'keyboard': '500\u20ac-1000\u20ac',
                           'mouse': '400\u20ac-500\u20ac'},
           'items_description': {'iPhone': 'Apple',
                                 'MacBook': 'Apple',
                                 'Nintendo': 'Nintendo',
                                 'Xbox': 'Micrasoft'}
           }

with open('product_2.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA_IN, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("product_2.yaml", 'r', encoding='utf-8') as f_out:
    DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
