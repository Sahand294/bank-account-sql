from flask import Flask,render_template,session,request,redirect,url_for
from prostgresssql.total import DataBase
from Filemanager import Filemanager
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
    return info
def wrong(info):
    info['id'] = 'invalid password'
    info['password'] = 'invalid password'
    info['owner'] = 'invalid password'
    info['balance'] = 'invalid password'
    info['type'] = 'invalid password'
app = Flask(__name__)
app.secret_key = "hi"
@app.route('/deposit', methods=['GET', 'POST'])
def deposit_website():
    if request.method == "POST":
        session['deposit-money'] = request.form['deposit-money']
        deposit()
        return redirect(url_for('home'))

    return render_template('deposit.html')
def transfer():
    money = 0
    pos_money = 0
    id = 0
    if 'transfer-money' in session:
        pos_money = int(session.get('transfer-money'))

        money = int(session.get('transfer-money'))
    money = 0 - money
    if 'account' in session:
        id = int(session.get('account'))
    Filemanager.changing_it('balance',int(session.get('id')),money)
    Filemanager.changing_it('balance',int(session.get('account')),pos_money)

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
    money = 0
    if 'deposit-money' in session:
        money = session.get('deposit-money')
    Filemanager.changing_it('balance',int(session.get('id')),int(money))
    # DataBase.update('the_entire_thing','balance',)
def withdraw():
    money = 0
    if 'deposit-money' in session:
        money = str(0 - int(session.get('withdraw-money')))
    Filemanager.changing_it('balance',int(session.get('id')),int(money))
@app.route('/display')
def home():
    info = {}
    if "id" in session:
        info = information(session.get('id'))
        if info['password'] != session.get('password'):
            wrong(info)
    return render_template("test.html",info=info)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session['id'] = request.form['id']
        session['password'] = request.form['password']
        return redirect(url_for('home'))
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)