import json

# загрузка данных из файла
def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# фильтр по выполненым операциям
def executed_operation(data):
    data = [item for item in data if item.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda item: item['date'], reverse=True)
    return data

# функция фильтрации нужных даннах
def formated_data(item):
    item_date = format_date(item.get("date"))

    if item.get("from"):
        from_ = mask_card(item.get("from")) + ': '
    else:
        from_ = ''

    return f'{item_date} {item.get("description")}\n' \
           f'{from_} {item.get("to")}\n' \
           f'{item["operationAmount"]["amount"]} {item["operationAmount"]["currency"]["name"]}\n'

# функция формата даты операции
def format_date(new_date):
    list_date = new_date[:10].split('-')
    return '.'.join(reversed(list_date))

# функция маскировки карты
def mask_card(card):
    card = card.split(' ')
    if card[0] == 'Счет':
        return f'{card[0]} {card[-1][:4]}'
    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'
