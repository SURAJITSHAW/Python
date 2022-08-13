# f-strings are particularly useful dynamically generated string. Just put a 'f' as prefix.
first_name = 'Surajit'
last_name = 'Shaw'
job = 'student'

# traditional way / tedious way
message = first_name + ' [' + last_name + ']' + ' is a ' + job + '. '
print(message) 

# modern way [f-strings]
msg = f'{first_name} [{last_name}] is a {job}. '
print(msg)