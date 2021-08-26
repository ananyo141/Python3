birthdays= {'Ananyo': '29 Apr',
 'Shrestha': '11 Nov',
 'Subhrajyoti': '11 Apr',
 'Subrata': '11 Jan',
 'Susmita': '1 March'}

# WAP to create a person name-birthdays dictionary so that the user can enter a name and get the corresponding 
# birthdays. Also, ask the user to add to the database if the prompted birthday is not found.
# This is a self-updating script. Edit with caution.

import pprint
while True:
    print("Enter a name:(blank to quit)")
    name=input()
    if name=='':
        break
    
    if name in birthdays:
        print(name, "has cake day on", birthdays[name])
    else:
        print("Birthday information not found for",name)
        bday=input("Please enter the their birthdays to update the database: ")
        birthdays[name]=bday
        print("Database successfully updated.Do you want to save the file?Y/N")
        choice = input()

        if choice=='Y' or choice=='y':
            file=open("findBirthday.py",mode='r')
            line = file.readline()
            while line!='\n':
                line=file.readline()
            content=file.readlines()
            file.close()

            file=open("findBirthday.py",mode='w')
            file.write('birthdays= '+ pprint.pformat(birthdays)+'\n')
            file.write('\n')
            for line in range(len(content)):
            	file.write(content[line])
            file.close()
            print("Process completed.")
            
        elif choice=='N' or choice=='n':
            print("You chose not to save the birth date.")
        else:
            print("You didn't enter a valid choice")
