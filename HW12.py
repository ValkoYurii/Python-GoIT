import pickle
import sys
import os.path
from collections import UserDict
import datetime
import re
import copy


file = 'data.bin'

class Field:
    def __init__(self) -> None:
        pass
class Name(Field):
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise Exception('Enter name.')
        else:
            self.__name = name
class Phone(Field):
    
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        new_value = str(new_value.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
        )
        if new_value.isdigit and len(new_value)>5:
            self.__value = new_value
        else:
            print('Phone number is wrong')
            self.__value = None
class AddressBook(UserDict):

  
    def add_record(self, name, record):
        self.data[name] = record
    
    def full_search(self, user_or_phone):
        result = ''

        for rec in self.data.values():
            if user_or_phone in rec.name.value:
                result += '\n' + str(rec)
            dig_user_or_phone = re.sub(r'[\D]', '', user_or_phone)
            if len(dig_user_or_phone) > 3:
                for phone in rec.phones:
                    if dig_user_or_phone in phone.value:
                        result += '\n' + str(rec)
    
    def iterator(self, n):
    
        something = self
        self.n = n
        self.i = 0
        while self.i < len(self.data): 
            yield str(list(next(self).items()))

    def __next__(self):
        if self.i >= len(self):
            raise StopIteration

        lst_items = list(self.data.items())
        cuter_items = dict(lst_items[self.i: self.i + self.N])

        self.i += self.N

        return cuter_items

    def __iter__(self, n=1):
        self.i = 0
        return self
class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        bd_num = re.split(r'[\.,\- /:]+', birthday)
        bd_num = ".".join(map(str, bd_num))
        try:
            date_of_birth = datetime.strptime(bd_num, '%d.%m.%Y')
            print(date_of_birth)
            if date_of_birth.date() >= datetime.today().date():
                print('Date from future')
                self.__birthday = None
                return
            self.__birthday = date_of_birth.date()
            return self.__birthday
        except:
            print('Wrong date. Date format \'dd.mm.yyyy\'')
            self.__birthday = None
class Record():
    def __init__(self, name, birthday=None):
        self.name = name
        self.birthday = birthday
        self.phones = []
    
    def days_to_birthday(self):
        time_range = day_now - self.birthday.birthday
        if time_range.days > 0:
            return time_range.days
        elif time_range.days == 0:
            return 0
        else:
            time_range = day_now.replace(year=day_now.year + 1) - self.birthday.birthday
            return time_range.days
        
    def add_phone(self, phone):
        phone = str(
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
        )
        self.phones.append(phone)
        return self.phones


def input_error(func):
    def hundler(data):
        try:
            result = func(data)
        except Exception as e:
            return e
        return result
    return hundler

@input_error
def hello(data):
    print("How can I help you?")

@input_error
def add_ph(data):
    data = data.replace('add ph ', '')
    if len(data.split()) == 2:
        name, phone = data.split()
        if name not in phone_book:
            new_name = Name(name)
            new_phone = Phone(phone)
            rec = Record(name=new_name, phone=new_phone)
            phone_book.add_record(rec)
        else:
            phone = Phone(phone)
            phone_book[name].add_phone(phone)

    else:
        raise Exception("Enter name and phone please")


@input_error
def add_bd(data):
    data = data.replace('add bd ', '')
    if len(data.split()) == 2:
        name, birthday = data.split()
        bd = Birthday(birthday)
        if name not in phone_book:
            new_name = Name(name)
            rec = Record(name=new_name, birthday=bd)
            phone_book.add_record(rec)
        elif phone_book[name].birthday.value == None:
            phone_book[name].change_birthday(bd)
        else:
            raise Exception("Birthday seted")

    else:
        raise Exception("Enter name and brthday please")


@input_error
def change_ph(data):
    data = data.replace('change ph ', '')
    if len(data.split()) == 3:
        name, phone, new_phone = data.split()
        if name in phone_book:
           phone_book[name].change_phone(Phone(phone), Phone(new_phone))
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Give me name and phone please")


@input_error
def change_bd(data):
    data = data.replace('change bd ', '')
    if len(data.split()) == 2:
        name,  new_birthday = data.split()
        if name in phone_book:
            new_birthday = Birthday(new_birthday)
            phone_book[name].change_birthday(new_birthday)
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Enter name and birthday, please")


@input_error
def phone(data):
    data = data.replace('phone ', '')
    if len(data.split()) == 1:
        name = data
        if name in phone_book:
            return phone_book[name]
        else:
            raise Exception("User is not found")
    else:
        raise Exception("Enter name")


@input_error
def show_all(data):
    data = data.replace('show all', '')
    if len(data.split()) == 1:
        try:
            N = int(data)
        except:
            N = 1
    else:
        N = len(phone_book.data)

    for el in phone_book.iterator(N):
        print(el)
        print('----------')
    return 'End'


@input_error
def find(data):
    data = data.replace('find ', '')
    if len(data.split()) == 1:
        result = phone_book.full_search(data)
        return result


@input_error
def good_bye(data):
    with open(file, 'wb') as f:
        pickle.dump(phone_book, f)
    return "Good bye!"


ACTIONS = {
    'hello': hello,
    'add ph': add_ph,
    'add bd': add_bd,
    'change ph': change_ph,
    'change bd': change_bd,
    'phone': phone,
    'show all': show_all,
    'find ': find,
    'good bye': good_bye,
    'close': good_bye,
    'exit': good_bye,
    '.': good_bye,
}


@input_error
def choice_action(data):
    for command in ACTIONS:
        if data.startswith(command):
            return ACTIONS[command]
    raise Exception("Enter command please")


if __name__ == '__main__':

    phone_book = AddressBook()
   
    if os.path.isfile(file):
        with open(file, 'rb') as f:
            phone_book = pickle.load(f)
   

    while True:
        text = ''' You can:
        add ph <name> <phone>
        add bd <name> <birthday>
        show all  <N>    - show all abonent, N - number abonents in page
        phone <name>  - show all phone this abonent
        change ph <name> <phone> <new_phone>
        change bd <name> <new_birthday>
        find <str>    - seek all records where is finding <str>
        hello, good bye, close, exit, . - to exit programm
        '''
        print(text)
        data = input()

        func = choice_action(data)
        if isinstance(func, Exception):
            print(func)
            continue
        result = func(data)
        if result:
            print(result)
        if result == 'Good bye!':
            break