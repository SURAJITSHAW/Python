customer = {
    'name': 'Surajit',
    'age': 19,
    'e-mail': 'surajit@gmail.com',
    'have_gf': True
}

customer['name'] = 'Shaw'
print(customer.get('have_gf', False))
print(customer)

# Challange 1
digits = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three'
}
user_input = input('Enter a number: ')

output = ''
for ch in user_input:
    output += digits.get(ch, '!') + ' '
print(output)