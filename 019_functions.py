# first define the funct then call it.
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
