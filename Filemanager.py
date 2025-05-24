from prostgresssql.total import DataBase
import json
from datetime import datetime

class Filemanager:
    @staticmethod
    def transactions(key, new_value, id, optional_transaction=False):
        time = datetime.now()
        with open('transactions.json', 'r') as file:
            fool = json.load(file)
            account = {}
            fool = fool
            for i in fool['accounts']:
                if id == i['id']:
                    account = i
                else:
                    account = {'id': id,'trans actions': []}
            # print(account,key,new_value,id)
        if optional_transaction:
            print('op',account, key, new_value, id)
            account['trans actions'].append(f'{optional_transaction} at {time.strftime("%Y-%m-%d %H:%M")}')
        elif key == 'password':
            print('password',account, key, new_value, id)
            account['trans actions'].append(f' has changed the password to {new_value} at {time.strftime("%Y-%m-%d %H:%M")}')
        elif key == 'owner':
            print('owner',account, key, new_value, id)
            account['trans actions'].append(f' has changed the owner name to {new_value} at {time.strftime("%Y-%m-%d %H:%M")}')
        elif key == 'balance':
            if float(new_value) > 0:

                account['trans actions'].append(f' has deposited {float(new_value)}$  balance:{Filemanager.check_status(id, 'balance')} at {time.strftime("%Y-%m-%d %H:%M")}')
            else:

                account['trans actions'].append(f' has withdraw {abs(float(new_value))}$  balance:{Filemanager.check_status(id, 'balance')} at {time.strftime("%Y-%m-%d %H:%M")}')
        lump = True
        for x,i in enumerate(fool['accounts']):
            if i['id'] == account['id']:
                fool['accounts'][x] = account
                lump=False
        if lump:
            fool['accounts'].append(account)
        with open('transactions.json','w') as file:
            json.dump(fool,file,indent=4)


    @staticmethod
    def checking_the_key(key):
        if key != 'balance':
            if key != 'password':
                if key != 'owner':
                    raise KeyError('no such key')
                else:
                    return True
            else:
                return True
        else:
            return True

    @staticmethod
    def check_status(id: int, key: str):
        Filemanager.checking_the_key(key)
        s = DataBase.read(f'the_entire_thing WHERE id = {id}')
        for i in s:
            a = i
        return a[f'{key}']

    @staticmethod
    def changing_it(key: str, id: int, new_value: str,op_tran=False):
        Filemanager.checking_the_key(key)
        if key == 'balance':
            t = Filemanager.check_status(id, 'balance')
            o = t + new_value
        else:
            o = new_value
        DataBase.update('the_entire_Thing', key, o, f'id = {id}')
        Filemanager.transactions(key,new_value,id,op_tran)

