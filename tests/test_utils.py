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

    assert executed_operation(list) == sorted_list


def test_format_date():
    assert format_date('2018-10-14T08:21:33.419441') == '14.10.2018'
    assert format_date('2018-01-26T15:40:13.413061') == '26.01.2018'
