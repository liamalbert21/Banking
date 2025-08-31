import actions

def user():
    user_options = ('Create Account', 'Add/Remove Pin', 'Deposit', 'Withdraw', 'Transfer',
                    'Check Balance', 'Print Statement', 'Admin', 'Exit')
    print()
    while True:
        print('=== NeoBank ===')
        for i, v in enumerate(user_options):
            print(f'{i+1}. {v}')
        print()
        choice = actions.get_input('Choice: ', int)
        match choice:
            case 1:
                actions.new_account()
            case 2:
                actions.add_remove_pin()
            case 3:
                actions.change_funds(True)
            case 4:
                actions.change_funds(False)
            case 5:
                actions.move_funds()
            case 6:
                actions.view(True)
            case 7:
                actions.view(False)
            case 8:
                print('Enter admin password. You have 3 attempts before lockout')
                if actions.login(admin_login = True):
                    admin()
                else:
                    return
            case 9:
                print('Thank you for banking with us!')
                return
            case _:
                print('Error: Invalid selection\n')

def admin():
    admin_options = ('Import Data', 'Export Database', 'Close User Account',
                     'Change Admin Password', 'Lock/Unlock Account', 'Logout')
    print()
    while True:
        print('=== Admin Panel ===')
        for i, v in enumerate(admin_options):
            print(f'{i+1}. {v}')
        print()
        choice = actions.get_input('Choice: ', int)
        match choice:
            case 1:
                actions.import_export(True)
            case 2:
                actions.import_export(False)
            case 3:
                actions.discard_account()
            case 4:
                actions.new_password()
            case 5:
                actions.lock_account()
            case 6:
                print()
                return
            case _:
                print('Error: Invalid selection\n')