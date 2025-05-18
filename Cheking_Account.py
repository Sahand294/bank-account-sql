from Bank_Account import BankAccount as Banks
from  Filemanager import Filemanager
class CheckingAccount(Banks):
    def __init__(self, account_holder, account_number, password, withdrawlimit,type):
        self.total_Review = {'owner': account_holder, 'id': account_number, 'balance': 0.0, 'type': 'checking',
                             'withdraw limit': withdrawlimit}
        super().__init__(account_holder, account_number, password,account_file,type)
        self.new_attribute = {'withdraw limit':withdrawlimit}

    def withdraw(self, money, password):
        if float(money) <= float(self.new_attribute['withdraw limit']):
            super().withdraw(money, password)
        else:
            raise Exception(f"you have hit the withdraw limit")
    def review(self):
        return {'owner': Filemanager.check_status(self.file, self.account_number,'owner'), 'id': self.account_number,
                'balance': Filemanager.check_status(self.file, self.account_number, 'balance'),'type':'checking'}

