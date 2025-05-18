from adding_accounts import Adding_Accounts
from abc import abstractmethod
adding_accounts = Adding_Accounts()
from Filemanager import Filemanager
from prostgresssql.total import DataBase
balances = Filemanager()


class BankAccount:
    def __init__(self, bank_holder, account_number, password,type):
        self.account_number = int(account_number)
        #self.file = account_file
        a = DataBase.read('the_entire_thing')
        error = True
        for i in a:
            if i['id'] == self.account_number:
                error = False
        if error:
            adding_accounts.adding_account(self.account_number, bank_holder,password,type)

    def changing_password(self, old_password, new_password):
        if old_password != Filemanager.check_status(self.account_number, 'password'):
            raise ValueError('the old password is not correct')

        Filemanager.changing_it('password',self.account_number, f"'{new_password}'")

    def changing_owner(self, password, owner_new_name):
        if password != Filemanager.check_status(self.account_number, 'password'):
            raise ValueError('the password is not correct')

        Filemanager.changing_it('owner',self.account_number, owner_new_name)

    def deposit(self, money):
        Filemanager.changing_it('balance',self.account_number, money)

    def withdraw(self, money, password):
        bill = 0 - money
        if Filemanager.check_status(self.account_number, 'balance') <= 0:
            raise Exception("don't have enouth money")
        if password != Filemanager.check_status(key='password', id=self.account_number):
            raise ValueError('incorrect passwrd')
        Filemanager.changing_it('balance',self.account_number, bill)

    def transfer(self, money, target_account, password):
        with open(f"transaction", 'a') as text:
            text.write(
                f'\n{self.account_number} has transferred {money}$ from {self.account_number} to {target_account} balance:{Filemanager.check_status(self.account_number,'balance')}')

        self.withdraw(money, password)
        target_account.deposit(money)

        with open(f"transaction", 'a') as text:
            text.write(
                f'\n{self.account_number} has transferred {money}$ from {self.account_number} to {target_account} balance:{Filemanager.check_status(self.account_number,'balance')}')
    @abstractmethod
    def review(self):
        return {'owner': Filemanager.check_status(self.account_number,'owner'), 'id': self.account_number,
                'balance': Filemanager.check_status(self.account_number, 'balance')}
