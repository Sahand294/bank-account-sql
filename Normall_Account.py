from Bank_Account import BankAccount as Banks
from Filemanager import Filemanager

class NormalAccount(Banks):
    def __init__(self, bank_holder, account_number, password,type):
        super().__init__(bank_holder, account_number, password,type)
        self.new_attribute = None
    def review(self):
        return 1
        #return {'owner': Filemanager.check_status( self.account_number,'owner'), 'id': self.account_number,
         #       'balance': Filemanager.check_status(self.account_number, 'balance'),'type':'normall'}

