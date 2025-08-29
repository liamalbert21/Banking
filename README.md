Banking project demonstrating principles of OOP and extended module use in Python. Current functionality is as follows (updated 8/29/2025):

**User Interface:**
- Create Account: Instantiates account object with random account number, specified balance, and unlocked status attributes
- Add Account Pin: **IN PROGRESS**
- Deposit: Increases account balance by specified amount
- Withdraw: Decreases account balance by specified amount
- Transfer: Increases origin account balance and decreases destination account balance by specficied amount
- Check Balance: Views account balance
- Print Statement: Views account transactions and itialization with corresponding dates and times
- Admin: Presents login interface for admin panel
- Exit: Ends the program

**Admin Interface:**
- Import Data: Imports user data from .xlsx file
- Export Database: Exports account data as .xlsx
- Remove Account: Removes account from database
- Create New Password: Modifies administrator password
- Lock/Unlock Account: Locks/unlcoks account
- Logout: Returns to user interface

**Notes:**
- Admin password is hashed using SHA-512
- Account name is limited to alphabetic characters and whitespace
- Locked accounts are restricted from account-specific actions
- "Import Data" function is inefficient for datasets containing > 100 accounts

**Future Plans:**
- Require passwords for data functions
- Add functionality for "Add Account Pin" option
- Optimize "Import Data" function
- Add GUI
- Encrypt/hash stored database
- Continual optimization/redundant code removal
