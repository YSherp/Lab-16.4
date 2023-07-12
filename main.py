import os
from datetime import datetime


def print_header(lab_name):
    current_directory = os.getcwd()
    user_profile = os.environ.get('USER')
    print(current_directory)
    print(f'Programmer: {user_profile}')
    time = datetime.now()
    current = time.strftime("%B %d, %Y @ %H:%M:%S")
    print(f'{lab_name} {current}\n')


def main():
    print_header('Lab 16.4')
    name = input('Enter your name: ')
    string = input('Enter a string: ')

    freq_dict = {}

    for char in string:
        freq_dict[char.upper()] = freq_dict.get(char.upper(), 0) + 1

    mode = max(freq_dict, key=freq_dict.get)

    print(f'{name}, the character that appears most frequently '
          f'in the string is {mode}')
    print(f'{mode} appears {freq_dict.get(mode)} times.')


if __name__ == '__main__':
    main()
