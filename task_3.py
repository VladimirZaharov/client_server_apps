import yaml


some_list = [
    'product_1',
    'product_2',
    'product_3'
]
some_number = 3948
some_dict = {
    'key_1': ord('ȧ'),
    'key_2': ord('Ȝ'),
    'key_3': ord('Ȥ')
}
base_dict = {
    'some_list': some_list,
    'some_number': some_number,
    'some_dict': some_dict
}
with open('file.yaml', 'w') as p:
    yaml.dump(base_dict, p, default_flow_style=False, allow_unicode=True)

with open('file.yaml', 'r') as q:
    new_dict = yaml.load(q)
    print(new_dict)
