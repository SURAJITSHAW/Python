# first define the funct then call it.
from turtle import end_fill


def greet_user():
    print('Hi there!')


greet_user()

# parameters [surajit is the argument, and name is the parameter here]
def greet_parameter(name):
    print(f'Hello {name}')


greet_parameter('Surajit')

# arguments are 2 types -> 1. postional & 2. keyword arguments
def greet_keyword_args(first_name, last_name):
    print(f'How are you doing {first_name} {last_name}!')


greet_keyword_args(last_name='Ghosh', first_name='Riya') # In keyword args postion doesn't matter


# Challange 1, put the logic of emoji convertor prog in a funct
message = input('> ')
def emoji_convertor(mes):
    emoji = {
        ':(': '😢',
        ':)': '😃'
    }
    words = mes.split(' ')
    output = ''
    for word in words:
        output += emoji.get(word, word) + ' '
    return output


print(emoji_convertor(message))

