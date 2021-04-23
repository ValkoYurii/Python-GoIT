import re
def nomilize(i):
    out = ''
    result = translate(i)
    out = re.sub(r'[^a-zA-Z0-9]', '_', result)


    print(out)

def translate(text):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
            "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

    TRANSLIT_DICT = {}
    output = ""
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANSLIT_DICT[ord(c)] = l
        TRANSLIT_DICT[ord(c.upper())] = l.upper()
    output = text.translate(TRANSLIT_DICT)
    return output

nomilize('Андрей,.,.:???sldk')
