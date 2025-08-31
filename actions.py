import re, hashlib, openpyxl, bank_data
from openpyxl.utils.exceptions import InvalidFileException

def login(pin = None, admin_login = False):
    if pin:
        verify = pin; input_type = int
    else:
        verify = bank_data.Bank.get_password(); input_type = str
    for x in range(3):
        attempt = get_input(f'Attempt {x+1}: ', input_type)
        if not pin:
            if hashlib.sha512(attempt.encode()).digest() == verify:
                return True
        elif attempt == verify:
            return True
        print('Incorrect')
    print('Login failed. User lockout\n') if admin_login else print('Login failed\n')
    return False

def check_account(account):
    if not account:
        return False
    elif account.is_locked:
        print('Error: Account is locked\n')
        return False
    if account.pin:
        print('Enter account pin. You have three attempts')
        if not login(pin = account.pin):
            return False
    return True

def get_input(prompt, cast):
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print('Error: Invalid input')

def new_account():
    name = get_input("Enter account holder's name: ", str)
    valid_name = True if not re.search(r'[^a-zA-Z\s]', name) else False
    if not valid_name:
        print("Error: Name must only contain alphabetic characters and whitespace\n")
        return
    start = get_input('Enter initial deposit: $', float)
    bank_data.Bank.create_account(name, start)

def add_remove_pin():
    account_number = get_input('Enter account number: ', int)
    account = bank_data.Bank.get_account(account_number)
    if not check_account(account):
        return
    if account.pin:
        account.pin = None
    else:
        pin = get_input('Enter desired pin: ', int)
        verify = get_input('Re-enter desired pin: ', int)
        if verify == pin:
            account.pin = pin
        else:
            print('Error: Pins do not match\n')
            return
    print('Success.\n')

def change_funds(is_deposit):
    account_number = get_input('Enter account number: ', int)
    account = bank_data.Bank.get_account(account_number)
    if check_account(account):
        action = 'deposit' if is_deposit else 'withdrawal'
        amount = get_input(f'Enter {action} amount: $', float)
        if is_deposit:
            account.deposit(amount)
        else:
            account.withdraw(amount)

def move_funds():
    origin = get_input('Enter origin account number: ', int)
    account_1 = bank_data.Bank.get_account(origin)
    if not check_account(account_1):
        return
    destination = get_input('Enter destination account number: ', int)
    account_2 = bank_data.Bank.get_account(destination)
    if not check_account(account_2):
        return
    amount = get_input('Enter transfer amount: $', float)
    bank_data.Bank.transfer(origin, destination, amount)

def view(is_balance):
    account_number = get_input('Enter account number: ', int)
    account = bank_data.Bank.get_account(account_number)
    if check_account(account):
        if is_balance:
            account.check_balance()
        else:
            account.print_statement()

def import_export(is_import):
    print('Enter admin password. You have 3 attempts')
    if login():
        if is_import:
            path = get_input('Enter file path: ', str)
            try:
                worksheet = openpyxl.load_workbook(path.strip(' "'), data_only = True).active
                print('In progress...')
                max_row = worksheet.max_row
                for row in range(2, max_row + 1):
                    name = worksheet.cell(row, 1).value
                    start = worksheet.cell(row, 2).value
                    status = True if worksheet.cell(row, 4).value else False
                    bank_data.Bank.create_account(name, start, status, True)
                print('Success.\n')
            except FileNotFoundError:
                print('Error: Invalid path\n')
            except InvalidFileException:
                print('Error: Invalid file format\n')
        else:
            bank_data.Bank.export_database()

def discard_account():
    account_number = get_input('Enter account number: ', int)
    if not bank_data.Bank.get_account(account_number):
        return
    verification = get_input('Re-enter account number: ', int)
    if account_number == verification:
        print('Warning: This change is irreversible')
        print('Enter admin password to confirm deletion. You have 3 attempts')
        if login():
            bank_data.Bank.remove_account(account_number)
    else:
        print('Error: Accounts do not match\n')

def new_password():
    print('Enter current admin password. You have 3 attempts')
    if login():
        desired_password = get_input('Enter new password: ', str)
        verification = get_input('Re-enter new password: ', str)
        if desired_password == verification:
            bank_data.Bank.change_password(desired_password)
        else:
            print('Error: Passwords do not match\n')

def lock_account():
    account_number = get_input('Enter account number: ', int)
    account = bank_data.Bank.get_account(account_number)
    verification = get_input('Re-enter account number: ', int)
    if account_number == verification:
        if not account:
            return
        access = 'locked' if account.is_locked else 'unlocked'
        print(f'This account is {access}')
        print('Enter admin password to change account status. You have 3 attempts')
        if login():
            account.is_locked = not account.is_locked
            print('Success.\n')
    else:
        print('Error: Accounts do not match\n')