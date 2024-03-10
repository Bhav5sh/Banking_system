import json


class Account:
    accounts_file='accounts_dp.json'
    def __init__(self, name, initial_deposit):
        self.account_number=self._get_new_account_number()
        self.name=name
        self.balance=initial_deposit
        self._save_new_account()
        print(f'Account created for { name }. Account Number: { self.account_number}')


    @classmethod
    def _load_accounts_db(cls):
        try:
            with open(cls.accounts_file,'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
    @classmethod
    def _save_accounts_db(cls,accounnts_db):
        with open(cls.accounts_file,'w') as file:
            json.dump(accounnts_db, file, indent=4)

    def _get_new_account_number(self):
        accounts_db=self._load_accounts_db()
        if accounts_db:
            return int(max(accounts_db.keys() , key=int)) + 1
        else:
            return 1

    def _save_new_account(self):
        accounts_db= self._load_accounts_db()
        accounts_db[self.account_number]= {'name': self.name , 'balance':self.balance}
        self._save_accounts_db(accounts_db)


class Balance:
    @staticmethod
    def check_balance(account_number):
        accounts_db=Account._load_accounts_db()
        if account_number in accounts_db :
            account_details=accounts_db[account_number]
            print(f"Account Number: { account_number} \n Account Holder: {account_details['name']} \n Balance: {account_details['balance']}")
        else:
            print('Account not found.')

class Deposit:
    @staticmethod
    def deposit_money(account_number, amount):
        accounts_db=Account._load_accounts_db()
        if account_number in accounts_db and amount>0:
            accounts_db[account_number]['balance'] += amount
            Account._save_accounts_db(accounts_db)
            print(f"Deposit money: {amount}. New Balance: {accounts_db[account_number]['balnace']}")
        else:
            print('Deposit failed. Please check the amount number and deposit mmoney. ')

class Withdrawal :
    @staticmethod
    def withdraw_money(account_number, amount):
        accounts_db=Account._load_accounts_db()
        if account_number in accounts_db and 0<amount<=accounts_db[account_number]['balance']:
            accounts_db[account_number]['balance'] -= amount
            Account._save_accounts_db(accounts_db)
            print(f"Withdrawal Amounnt {amount}. Remaining Balance : {accounts_db[account_number]['balance']}")
        else:
            print('Withdrawal faield. Please check the account number and withdrawal amount.')



# code driven
            
acc1=Account('John', 1000)
acc2=Account('Bhavesh', 2000)
Balance.check_balance(1)
Balance.check_balance(2)
Deposit.deposit_money(1, 500)
Deposit.deposit_money(2, 1000)
Balance.check_balance(1)
Balance.check_balance(2)




            