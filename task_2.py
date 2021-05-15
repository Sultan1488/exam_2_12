f = open('text.txt', 'r')
text_1 = f.read()


def get_letters(text):
    list_1 = []
    for i in text.lower():
        if i == 's' or i == 't':
            list_1 .append(i)
        if i == 'advert':
            i.upper():


    new_string = ''.join(list_1)
    new_dict = {letter: new_string.count(letter) for letter in new_string}
    return new_dict

    

dict_1 = get_letters(text_1)
print(dict_1)