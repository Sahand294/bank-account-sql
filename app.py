from flask import Flask,render_template,session,request,redirect,url_for
from prostgresssql.total import DataBase
from Filemanager import Filemanager
from Bank_Account import BankAccount
import json

def information(id):
    info = {}
    temp = DataBase.read('the_entire_Thing')
    all = {}
    for i in temp:
        if i['id'] == int(id):
            all = i
    info['id'] = all['id']
    info['owner'] = all['owner']
    info['password'] = all['password']
    info['balance'] = all['balance']
    info['type'] = all['type']
    info['error'] = ''
    return info
def wrong(info):
    info['id'] = 'invalid password'
    info['password'] = 'invalid password'
    info['owner'] = 'invalid password'
    info['balance'] = 'invalid password'
    info['type'] = 'invalid password'
app = Flask(__name__)
app.secret_key = "hi"
signin = False
@app.route('/deposit', methods=['GET', 'POST'])
def deposit_website():
    if request.method == "POST":
        session['deposit-money'] = request.form['deposit-money']
        deposit()
        return redirect(url_for('home'))

    return render_template('deposit.html')
@app.route('/signin',methods=['GET','POST'])
def sign_in_page():
    global signin
    if request.method == 'POST':
        session['sign_in_owner'] = request.form['sign_in_owner']
        session['sign_in_id'] = request.form['sign_in_id']
        session['sign_in_password'] = request.form['sign_in_password']
        session['sign_in_type'] = request.form['sign_in_type']
    signin = True
    if 'sign_in_id' in session:
        owner = session.get('sign_in_owner')
        id = session.get('sign_in_id')
        password = session.get('sign_in_password')
        type = session.get('sign_in_type')
        a = BankAccount(owner,id,password,type)
        return redirect(url_for('login'))
    return render_template('signin.html')
def transfer():
    money = 0
    pos_money = 0
    current_money = 0
    id = 0
    if 'transfer-money' in session:
        pos_money = int(session.get('transfer-money'))
        current_money = int(Filemanager.check_status(session['id'],'balance'))
        money = int(session.get('transfer-money'))
    money = 0 - money
    if 'account' in session:
        id = int(session.get('account'))
    neg_money = current_money + int(money)
    if int(money) > current_money or neg_money < 0 or current_money == 0:
        session['error'] = 'You do not have the amount of money needed for this withdraw'
    else:
        session['error'] = ''
        Filemanager.changing_it('balance',int(session.get('id')),money,op_tran=f'has transfered {pos_money} to the account {int(session.get('account'))}')
        Filemanager.changing_it('balance',int(session.get('account')),pos_money,op_tran=f'has recieved {pos_money} from the account {int(session.get('id'))}')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer_website():
    if request.method == "POST":
        session['transfer-money'] = request.form['transfer-money']
        session['account'] = request.form['account']
        transfer()
        return redirect(url_for('home'))
    return render_template('transfer.html')
@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw_website():
    if request.method == "POST":
        session['withdraw-money'] = request.form['withdraw-money']
        withdraw()
        return redirect(url_for('home'))
    return render_template('withdraw.html')
def deposit():
    session['error'] = ''
    money = 0
    if 'deposit-money' in session:
        money = session.get('deposit-money')
    Filemanager.changing_it('balance',int(session.get('id')),int(money))
    # DataBase.update('the_entire_thing','balance',)
def withdraw():
    money = 0
    current_money = 0
    if 'deposit-money' in session:
        money = str(0 - int(session.get('withdraw-money')))
        current_money = int(Filemanager.check_status(session['id'],'balance'))

    neg_money = int(current_money) + int(money)
    if int(money) > current_money or neg_money < 0 or current_money == 0:
        session['error'] = 'You do not have the amount of money needed for this withdraw'
    else:
        session['error'] = ''
        Filemanager.changing_it('balance',int(session.get('id')),int(money))
@app.route('/display')
def home():

    info = {}
    if "id" in session:
        info = information(session.get('id'))
        if info['password'] != session.get('password'):
            wrong(info)
    if 'error' in session:
        info['error'] = session.get('error')
    return render_template("test.html",info=info)
@app.route('/history')
def history():
    text = trans()
    return render_template('history.html',trans=text)

@app.route('/', methods=['GET', 'POST'])
def login():
    global signin
    if signin:
        signin = False
        del session['sign_in_owner']
        del session['sign_in_id']
        del session['sign_in_password']
        del session['sign_in_type']
    if request.method == "POST":
        session['id'] = request.form['id']
        session['password'] = request.form['password']
        return redirect(url_for('home'))

    return render_template("login.html")

def trans():
    with open('transactions.json','r') as file:
        text = json.load(file)
        for i in text['accounts']:
            if int(i['id']) == int(session.get('id')):
                return i['trans actions']

if __name__ == "__main__":
    app.run(debug=True, port=3000)