
# person = 'moses'
# index = 0
# while index < len(person):
#     print('present')
#     index += 1

# a function that gets initials of your names
# def get_initials(name):
#     initials = name[:1]
#     return initials


# first_name = input('first name: ')
# last_name = input('last name: ')

# firstname_initials = get_initials(first_name)
# lastname_initials = get_initials(last_name)

# print('Your initials are ' + firstname_initials + lastname_initials)


# use name notation when calling a function to make your code more readable

# this function logs us errors to the database.


def error_mode(error_code, error_severity, log_to_db, error_message, source_model):
    print('oh no error ' + error_message)


members = 30
present = 21

if members > present:
    error_mode(error_code=4, error_severity=1, log_to_db=True,
               error_message='members not complete', source_model='my_math_method')

# when using name notations gives you the chance to pass parameters in any other
