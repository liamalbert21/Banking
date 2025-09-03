Abstract: Back-end banking project demonstrating principles of OOP and extended module use in Python.

**Updates (9/3/2025):**
- Added Force Remove Pin admin function
- Organized code and logic for consistency

Current functionality is as follows:

**User Interface:**
- Create Account: Instantiates account object with random account number, balance, and unlocked status attributes
- Add Account Pin: Adds/removes account-specific pin
- Deposit: Increases account balance by specified amount
- Withdraw: Decreases account balance by specified amount
- Transfer: Increases origin account balance and decreases destination account balance by specified amount
- Check Balance: Displays account balance
- Print Statement: Displays account initialization and transactions with corresponding dates and times
- Admin: Presents login interface for admin panel
- Exit: Ends the program

**Admin Interface:**
- Import Data: Imports user data from .xlsx file
- Export Database: Exports account data as .xlsx file
- Remove Account: Removes account from database
- Create New Password: Modifies administrator password
- Force Remove Pin: Removes account pin regardless of locked status
- Lock/Unlock Account: Locks/unlocks account
- Logout: Returns to user interface

**Notes:**
- Administrator password is hashed using SHA-512
- Account names are limited to alphabetic characters and whitespace
- Account pins are limited to numeric characters
- Locked accounts are restricted from user-specific actions
- User-specific actions are locked behind pin for accounts with real pin attribute 
- "Import Data" function is inefficient for datasets containing > 100 accounts

**Future Plans:**
- Optimize "Import Data" function
- Add GUI/design website (import HTML/CSS for layout, SQL for cloud data)
- Encrypt/hash stored database
- Continual optimization/redundant code removal
