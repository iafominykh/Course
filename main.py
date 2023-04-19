from utils.utils import load_json, executed_operation, formated_data

# константа
JSON_FILE = '/home/test/PycharmProjects/Course//operations.json'

# основная функция
def main():
    data = load_json(JSON_FILE)
    data = executed_operation(data)

    for i in range(5):
        print(formated_data(data[i]))


if __name__ == '__main__':
    main()
