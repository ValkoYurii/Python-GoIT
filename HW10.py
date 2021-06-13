from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, name, record):
        self.data[name] = record
class Record(self):
    def __init__(self, name, *phones):
        self.phones = []
        self.name = name
    def add_phone(self, phone):
        self.phones.append(phone)
    def remove_phone(self, phone):
        self.phones.remove(phone)
    def edit_phone(self, phone):
        pass

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, value):
        self.value = value