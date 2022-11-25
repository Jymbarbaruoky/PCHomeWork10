from Home_Work_10 import AddressBook, Record

dict_contacts = AddressBook()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Wrong name'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Pls print: name and number'
        except TypeError:
            return 'Wrong command.'
    return inner

@input_error
def hello() -> str:
    return "How can I help you?"

@input_error
def add(data: list) -> None:
    if not (data[1]).isnumeric():
        raise ValueError
    if dict_contacts and data[0] in dict_contacts:
        record = Record(data[0])
        record.phones = dict_contacts[data[0]]
        if data[1] in record.phones:
            raise ValueError(f'This phone alredy exist in {data[0]}')
    else:
        record = Record(data[0])
    record.add_phone(data[1])
    dict_contacts.add_record(record)

@input_error
def change(data: list) -> None:
    if not (data[1]).isnumeric() or not (data[2]).isnumeric():
        raise ValueError
    record = Record(data[0])
    record.phones = dict_contacts[data[0]]
    record.editing(data[1], data[2])

@input_error
def phone(data: list) -> str:
    return dict_contacts[data[0]]

@input_error
def show_all() -> dict:
    if not dict_contacts:
        return 'The contact list is empty'
    return dict_contacts

@input_error
def end_program():
    return 'Good bye!'

def wrong_comand():
    return 'Wrong comand!'

OPERATIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': end_program,
    'close': end_program,
    'exit': end_program,
    'wrong comand': wrong_comand
}


def get_hendler(processed_comand):
    if processed_comand not in OPERATIONS:
        return OPERATIONS['wrong comand']
    return OPERATIONS[processed_comand]


def comand_parser(comand):
    result = {
        'comand': '',
        'data': []
    }
    if comand.lower() == 'show all' or comand.lower() == 'good bye':
        result['comand'] = comand.lower()
        return result['comand'], result['data']
    data_list = comand.split(' ')
    result['comand'] = data_list[0].lower()
    result['data'] = data_list[1:]
    return result['comand'], result['data']



def main() -> None:
    while True:
        comand = input('Waiting comand: ')
        processed_comand, data = comand_parser(comand)
        if data:
            result = get_hendler(processed_comand)(data)
        if not data:
            result = get_hendler(processed_comand)()
        if type(result) is dict:
            for key, value in result.items():
                print('{:<15} {:>15}'.format(key, value))
                continue
        elif result:
            print(result)
            if result == 'Good bye!':
                break



if __name__ == '__bot__':
    print('Program start')
    main()
