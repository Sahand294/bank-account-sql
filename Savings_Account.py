from Bank_Account import BankAccount as Banks
from Filemanager import Filemanager as balance

class SavingsAccount(Banks):
    def __init__(self, bank_holder, account_Number, password, intrest_Rate,type):
        self.new_attribute = {'interest rate':intrest_Rate}
        self.total_Review = {'owner': bank_holder, 'id': account_Number, 'balance': 0.0, 'type': 'savings',
                             'interest rate': intrest_Rate}
        super().__init__(bank_holder, account_Number, password,type)


    def apply_intrest(self):
        self.deposit(balance.check_status(self.account_number,'balance') * (float(self.new_attribute['interest rate']) / 100.0))
    def review(self):
        return {'owner': balance.check_status(self.account_number,'owner'), 'id': self.account_number,
                'balance': balance.check_status(self.account_number, 'balance'),'type':'savings'}
