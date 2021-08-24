# Simple timesheet that tracks the punch-in and punch-out time of employees
import time, datetime

login_database = {}

def main():
    # create a nested dictionary data-type that tracks the entry and exit of employees
    while True:
        name = input("Enter name: ")
        if name == 'exit':
            break
        if name in login_database:
            exit_time = time.time()
            login_database[name]['exit'] = exit_time
            print(f"Exit Registered, {name} at {time.ctime(exit_time)}")
        else:
            entry_time = time.time()        
            login_database.setdefault(name, {'entry': entry_time, 'exit': None})
            print(f"Entry Registered, {name} at {time.ctime(entry_time)}")

    # print the log for the employees
    print("\n" + "Total employees database:".center(50, "*"))
    for employee, data in login_database.items():
        print(employee.center(50))
        print(f"Entry at {time.ctime(data['entry'])}".center(50))
        if data['exit']:
            print(f"Exit at {time.ctime(data['exit'])}".center(50))
            time_spent = datetime.timedelta(seconds = data['exit'] - data['entry'])
            print(f"Total time spent {str(time_spent)}".center(50))
        else:
            print(f"{employee} didn't check out".center(50))
        print(''.center(50, '-'))

if __name__ == '__main__':
    main()
