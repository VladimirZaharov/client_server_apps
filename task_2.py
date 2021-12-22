import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'r') as f_n:
        objs = json.load(f_n)

    objs['orders'].append(dict_to_json)

    with open('orders.json', 'w') as p:
        print(objs)
        print(objs['orders'])
        json.dump(objs, p, indent=4)

write_order_to_json('shoes', 30, 3580, 'Zhukov', '23.12.20')

