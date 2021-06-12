import re
from collections import UserDict
from datetime import datetime, timedelta, date


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

    ad_b = AddressBook()
bd=Birthday("22-12-2020")
rec = Record("Vasya", bd)
ph1=rec.add_phone('92387289')
ph2=rec.add_phone('984654654')

print(rec.days_to_birthday())
