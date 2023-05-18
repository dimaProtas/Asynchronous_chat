import yaml

DATA_IN = {'items': ['iPhone', 'MacBook', 'Nintendo', 'Xbox'],
           'items_quantity': 4,
           'items_ptice': {'iPhone': '800€-1000€',
                           'MacBook': '1000€-1500€',
                           'Nintendo': '500€-1000€',
                           'Xbox': '400€-500€'},
           'items_description': {'iPhone': 'Apple',
                                 'MacBook': 'Apple',
                                 'Nintendo': 'Nintendo',
                                 'Xbox': 'Micrasoft'}
           }

with open('product.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA_IN, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("product.yaml", 'r', encoding='utf-8') as f_out:
    DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
