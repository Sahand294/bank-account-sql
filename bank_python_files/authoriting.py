from bank_python_files.Cheking_Account import CheckingAccount
from bank_python_files.Savings_Account import SavingsAccount
from bank_python_files.Normall_Account import NormalAccount
from prostgresssql.total import DataBase
c = CheckingAccount
n = NormalAccount
s = SavingsAccount


class Authoritize:
    @staticmethod
    def loging_in(password, id, **kwargs_):
        p = DataBase.read(f'the_entire_thing WHERE id = {id}')
        for i in p:
            u = i
        if password != u['password']:
            raise ValueError('wrong password')
        if u['type'] == 'checking':
            if 'withdraw_limit' not in kwargs_:
                raise ValueError('you have to give the withdraw limit')
            r = c(u['owner'], u['id'], u['password'], int(kwargs_.get('withdraw_limit')),'cheking')
        elif u['type'] == 'saving':

            if 'interest_rate' not in kwargs_:
                raise ValueError('you have to give the interest rate')

            r = s(u['owner'], u['id'], u['password'], int(kwargs_.get('interest_rate')), 'saving')
        elif u['type'] == 'normall':
            r = n(u['owner'], u['id'], u['password'],'normall')
        else:
            raise ValueError('no such type')
        return r
