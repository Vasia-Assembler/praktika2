import re


def is_good(pass_str):
    digits = re.search("[0-9]", pass_str) is not None
    characters_diff_case = (re.search('[a-z]', pass_str) is not None) and (re.search('[A-Z]', pass_str) is not None)
    special_characters = re.search('[!@#$%^&*(),.]', pass_str) is not None
    return digits and characters_diff_case and special_characters


p = input('Введите пароль: ')
good = False
while not good:
    if is_good(p):
        print('Пароль хороший.')
        good = True
    else:
        print('Плохой пароль!')
        p = input('Введите пароль: ')
