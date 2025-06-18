from prostgresssql.total import DataBase

class Adding_Accounts:
    field_names = 'owner,id,balance'
    def adding_account(self,account_number, bank_holder,password,type):
        field_names = 'owner,id,balance'
        DataBase.insert('the_entire_thing','id,owner,password,balance,type',f"({account_number},'{bank_holder}','{password}',0,'{type}')")