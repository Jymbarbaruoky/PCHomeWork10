from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, value):
        self.value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        print(f"You added {phone} to {self.name.value}")

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                print(f"You remove {phone} from {self.name.value}")
                return True
        return False

    def editing(self, old_phone, new_phone):
        if self.delete_phone(old_phone):
            self.add_phone(new_phone)

    def get_contacts(self):
        result = []
        for phone in self.phones:
            result.append(phone.value)
        return result


class AddressBook(UserDict):

    def add_record(self, Record):
        self.data[Record.name.value] = Record


        