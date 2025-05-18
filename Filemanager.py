from prostgresssql.total import DataBase

class Filemanager:
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
    def changing_it(key: str,id: int, new_value: str):
        Filemanager.checking_the_key(key)
        if key == 'balance':
            t  = Filemanager.check_status(id,'balance')
            o = t + new_value
        else:
            o = new_value
        DataBase.update('the_entire_Thing',key,o,f'id = {id}')


        if key == 'password':
            with open(f"transaction", 'a') as text:
                text.write(f'\n{id} has changed the password to {new_value}')
        elif key == 'owner':
            with open(f"transaction", 'a') as text:
                text.write(f'\n{id} has changed the owner name to {new_value}')
        elif key == 'balance':
            if float(new_value) > 0:
                with open(f"transaction", 'a') as text:
                    text.write(
                        f'\n{id} has deposited {float(new_value)}$  balance:{Filemanager.check_status(id, 'balance')}')
            else:
                with open(f"transaction", 'a') as text:
                    text.write(
                        f'\n{id} has withdraw {float(new_value)}$  balance:{Filemanager.check_status(id, 'balance')}')
