from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value]=record

class Record(self):
    def __init__(self, name, *phones):
        self.phones = []
    def name(self):
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
    pass

class Phone(Field):
    pass