from utils.utils import load_json, executed_operation, formated_data, format_date, mask_card


def test_load_json():
    list_ = [
        {
            "id": 615064591,
            "state": "CANCELED",
            "date": "2018-10-14T08:21:33.419441",
            "operationAmount": {
                "amount": "77751.04",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на счет",
            "from": "Maestro 3928549031574026",
            "to": "Счет 84163357546688983493"
        }
    ]
    assert load_json('test.json') == list_


def test_executed_operation():
    list_ = [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2019-08-19T04:27:37.904916"
        },
        {
            "id": 476991061,
            "state": "CANCELED",
            "date": "2018-11-23T17:47:33.127140"
        },
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2021-04-14T19:35:28.978265"
        }
    ]

    sorted_list = [
        {
            "id": 649467725,
            "state": "EXECUTED",
            "date": "2021-04-14T19:35:28.978265"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2019-08-19T04:27:37.904916"
        }

    ]

    assert executed_operation(list_) == sorted_list


def test_format_date():
    assert format_date("2018-06-12T07:17:01.311610") == "12.06.2018"
    assert format_date("2019-07-12T08:11:47.735774") == "12.07.2019"


def test_mask_card():
    assert mask_card("Счет 90562872508279542248") == "Счет 9056"
    assert mask_card("MasterCard 8532498887072395") == "MasterCard 8532 49** **** 2395"
    assert mask_card("МИР 8201420097886664") == "МИР 8201 42** **** 6664"


def test_formated_data():
    dict_1 = {
        "id": 988276204,
        "state": "EXECUTED",
        "date": "2018-02-22T00:40:19.984219",
        "operationAmount": {
            "amount": "71771.90",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "MasterCard 4956649687637418",
        "to": "Счет 90562872508279542248"
    }
    dict_2 = {
        "id": 172864002,
        "state": "EXECUTED",
        "date": "2018-12-28T23:10:35.459698",
        "operationAmount": {
            "amount": "49192.52",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 96231448929365202391"
    }

    str_1 = '22.02.2018 Перевод организации\n' \
            'MasterCard 4956 64** **** 7418 -> Счет **2248\n' \
            '71771.90 USD\n'
    str_2 = '28.12.2018 Открытие вклада\n' \
            'Счет **2391\n' \
            '49192.52 USD\n'

    assert formated_data(dict_1) == str_1
    assert formated_data(dict_2) == str_2