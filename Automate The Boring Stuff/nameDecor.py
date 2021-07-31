# WAP to decorate name entered by the user.

first_name=input("Enter your first name: ")
last_name=input("Enter you last name: ")
for char in first_name:
    print('****', char, '****')
print('\n')
for char in last_name:
    print('----',char,'----')
