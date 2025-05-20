from Normall_Account import NormalAccount
from Savings_Account import SavingsAccount
from Cheking_Account import CheckingAccount
from authoriting import Authoritize


class Bank:
    #hi
    def __init__(self):
        self.__accounts = {}

    def addaccounts(self, account_Type, account_holder, account_number, password, **kwargs_):
        if account_Type == 'cheking':
            limit = kwargs_.get('withdrawlimit', 1)
            self.__accounts[int(account_number)] = {'password': password,
                                                    'account': CheckingAccount(account_holder, account_number, password,
                                                                               int(limit), 'cheking')}
        # return
        if account_Type == 'saving':
            self.__accounts[int(account_number)] = {'password': password,
                                                    'account': SavingsAccount(account_holder, account_number, password,
                                                                              kwargs_.get('interestrate', 5),
                                                                              'saving')}
            # return
        if account_Type == 'normall':

            self.__accounts[int(account_number)] = {'password': password,
                                                    'account': NormalAccount(account_holder, account_number, password,
                                                                             'normall')}
            # return NormalAccount(account_holder, account_number, password, self.file)


bank1 = Bank()
a = Authoritize.loging_in('roshs',180,interest_rate=100)
b = Authoritize.loging_in('1391',200)
b.review()



