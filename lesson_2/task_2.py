import json


def write_order_to_json(item, quantity, price, buyer, date):

    with open('orders.json', 'r', encoding='utf-8') as f_out:
        data = json.load(f_out)

    with open('orders.json', 'w', encoding='utf-8') as f_in:
        orders_list = data['orders']
        order_info = {'item': item, 'quantity': quantity,
                      'price': price, 'buyer': buyer, 'date': date}
        orders_list.append(order_info)
        json.dump(data, f_in, indent=4)



# Указав кирилицу получаем "\u0424\u0435\u0434\u043e\u0440 \u0421\u043c\u043e\u043b\u043e\u0432"
# На латинице все ок
write_order_to_json('iPhone 14', '2', '82000', 'Hakimi Ashraf', '5.04.2023')
write_order_to_json('MacBook Pro', '1', '120000', 'Messi Leonel', '6.04.2023')
write_order_to_json('Nintendo', '4', '62000', 'Zinedin Zidan', '7.04.2023')
write_order_to_json('Xbox', '2', '59000', 'Федор Смолов', '4.03.2023')


#Мой вариант записи в json файл
def write_json(name, year, job, bonus):
    with open('bonus.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        resullt = data['bonus']
        info = {'name': name, 'year': year, 'job': job, 'bonus': bonus}
        resullt.append(info)
    with open('bonus.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

write_json('Dima', '31', 'couch', '5000')
