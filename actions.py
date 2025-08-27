import re, openpyxl, hashlib, bank_data

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
        print("Error: Name must only contain alphabetic characters and spaces\n")
        return
    start = get_input('Enter initial deposit: $', float)
    bank_data.Bank.create_account(name, start)

def change_funds(add):
    account_number = get_input('Enter account number: ', int)
    account = bank_data.Bank.get_account(account_number)
    if not account:
        return
    elif account.is_locked:
        print('Error: Account is locked\n')
        return
    action = 'deposit' if add else 'withdrawal'
    amount = get_input(f'Enter {action} amount: $', float)
    if add:
        account.deposit(amount)
    else:
        account.withdraw(amount)

def move_funds():
    origin = get_input('Enter origin account number: ', int)
    account_1 = bank_data.Bank.get_account(origin)
    if not account_1:
        return
    elif account_1.is_locked:
        print('Error: Account is locked\n')
        return
    destination = get_input('Enter destination account number: ', int)
    account_2 = bank_data.Bank.get_account(destination)
    if not account_2:
        return
    elif account_2.is_locked:
        print('Error: Account is locked\n')
        return
    amount = get_input('Enter transfer amount: $', float)
    bank_data.Bank.transfer(origin, destination, amount)

def view_balance():
    account_number = get_input('Enter account number: ', int)
    account = bank_data.Bank.get_account(account_number)
    if account:
        if account.is_locked:
            print('Error: Account is locked\n')
        else:
            account.check_balance()

def view_statement():
    account_number = get_input('Enter account number: ', int)
    account = bank_data.Bank.get_account(account_number)
    if account:
        if account.is_locked:
            print('Error: Account is locked\n')
        else:
            account.print_statement()

def login():
    current_password = bank_data.Bank.get_password()
    for x in range(3):
        attempt = hashlib.sha512(get_input(f'Attempt {x+1}: ', str).encode()).digest()
        if attempt == current_password:
            return True
        else:
            print('Incorrect')
    return False

def import_export(is_import):
    if is_import:
        path = get_input('Enter file path: ', str)
        try:
            workbook = openpyxl.load_workbook(path.strip(' "'))
            print('In progress...')
            worksheet = workbook.active
            max_row = worksheet.max_row
            for row in range(2, max_row + 1):
                name = worksheet.cell(row, 1).value
                start = worksheet.cell(row, 2).value
                status = False if worksheet.cell(row, 4).value else True
                bank_data.Bank.create_account(name, start, status, True)
            print('Success.\n')
        except:
            print('Error: Invalid path or file format\n')
    else:
        print('In development\n')
        # Export file with 4 columns: Account Name, Balance, Status, and Status (B) (Binary Status)

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
            print()
    else:
        print('Error: Accounts do not match\n')

def new_password():
    print('Enter current password. You have 3 attempts')
    if not login():
        print()
        return
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
        if not login():
            print()
            return
        account.is_locked = not account.is_locked
        print('Success.\n')
    else:
        print('Error: Accounts do not match\n')