Back-end banking project demonstrating principles of OOP and extended module use in Python.
Current functionality is as follows (updated 8/30/2025):

**User Interface:**
- Create Account: Instantiates account object with random account number, specified balance, and unlocked status attributes
- Add Account Pin: Adds/removes account-specific pin
- Deposit: Increases account balance by specified amount
- Withdraw: Decreases account balance by specified amount
- Transfer: Increases origin account balance and decreases destination account balance by specified amount
- Check Balance: Views account balance
- Print Statement: Views account transactions and initialization with corresponding dates and times
- Admin: Presents login interface for admin panel
- Exit: Ends the program

**Admin Interface:**
- Import Data: Imports user data from .xlsx file
- Export Database: Exports account data as .xlsx file
- Remove Account: Removes account from database
- Create New Password: Modifies administrator password
- Lock/Unlock Account: Locks/unlocks account
- Logout: Returns to user interface

**Notes:**
- Administrator password is hashed using SHA-512
- Account names are limited to alphabetic characters and whitespace
- Account pins are limited to numbers
- Locked accounts are restricted from user-specific actions
- User-specific actions are locked behind pin for accounts with pin attribute 
- "Import Data" function is inefficient for datasets containing > 100 accounts

**Future Plans:**
- Optimize "Import Data" function
- Add GUI/design website (import HTML/CSS for layout, SQL for cloud data)
- Encrypt/hash stored database
- Continual optimization/redundant code removal
