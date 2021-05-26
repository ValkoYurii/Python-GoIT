import re

def error_hendler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print(f'\nInvalid command. Try again...')
            return back_to_main
        except IndexError:
            print('\nEnter name and phone.')
            return back_to_main(*args, **kwargs)
    return inner

@error_hendler
def parser(string):
    
    regex = re.compile('\s+')
    string = regex.sub(' ', string)
    return string.split(' ')


@error_hendler
def add(command):
    if command[1] in contacts:
        return f'\nThe contact is already exist. To change the number, use the command "change".'
    else:
        contacts[command[1]] = command[2]
    return f'\nContact {command[1]} has been added.'

def back_to_main(*args, **kwargs):
    return f''

@error_hendler
def change(command):
    contacts.update({command[1]: command[2]})
    return f'\nContact {command[1]} has been updated.'

@error_hendler
def get_handler(command):
    return COMMANDS[command]

def hello(*args):
    return f'\nHow can I help you?'


@error_hendler
def phone(command):
    
    if command[1] in contacts:
        return f'\n{command[1]}: {contacts.get(command[1])}'
    else:
        return f'\nContact doesn\'t exist.'

def show_all(*args):
    result = ''
    for key, value in contacts.items():
        result += f'\n{key} : {value}'
    return result

COMMANDS = {
            'hello': hello,
            'add': add,
            'change': change,
            'phone': phone,
            'show': show_all
            }

EXIT_COMMANDS = {
                'exit': '',
                'close': '',
                'good': '',
                '.':''}
contacts = {}

@error_hendler
def main():
    while True:
        string = input('\nEnter your command: >>> ')
        command = parser(string)
        if command[0].lower() in EXIT_COMMANDS:
            print('Exit. Good bay!')
            break
        else:
            print(get_handler(command[0].lower())(command))

if __name__ == "__main__":
    main()