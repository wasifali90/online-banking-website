from flask import Flask , jsonify, render_template, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from mongoengine import connect
from models import User ,transfer

import json
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

def connect_to_db():
    connect("test",host = "mongodb+srv://sushrut69:Qwerty123@cluster0.hea5x0y.mongodb.net/test")
    
    
@app.route('/')
def index():
    return render_template("index.html")
    



@app.route('/home',methods = ['GET', 'POST'])
def home_page():
    connect_to_db()
    # u = User(email = "test@cluster0.hea5x0y.mong" ,name = "test" , amount = 100 , user_id = 2)
    # u.save()
    
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        amount = request.form.get('amount')
        # user_id = request.form.get('user_id')
        
        u1 = User(email=email, name = name , amount = amount)
        u1.save()
    
    # print(request.form)
    return render_template('homepage.html')




@app.route('/Customers',methods =   ['GET'])
def Customers():
    connect_to_db()
    if request.method == 'GET':
        users = User.objects()
        # customers = ['email', 'name','amount','user_id']
    res = render_template('Customers.html' , users = users )
    
    return res


@app.route('/transfer',methods = ['POST','GET'])
def Transfer():
    connect_to_db()
    transactions = []
    transfer_to = request.args.get('to_email')
    print(transfer_to)
    users = User.objects()
    # t1 = transfer(to_email = 'sushrut949@gmail.com' , from_email = 'test@gmail.com', amount = 1)
    # t1.save()
    
    if request.method == 'POST':
        to_email = request.form.get('to_email')
        from_email = request.form.get('from_email')
        amount = request.form.get('amount')
         
        
        t1 = transfer(to_email = to_email, from_email = from_email, amount = amount)
        t1.save()
        
        
    return render_template('Transfer.html',transfer_to = transfer_to , users = users)
        
    # if request.method == 'GET':
    #     transactions = transfer.objects()
    # res =  render_template('transfer.html' , transactions = transactions)
    # print(res)
    # return res
    
        
        
@app.route('/transactionHistory', methods = ['GET'])
def TransactionHistory():
    connect_to_db()
    if request.method == 'GET':
        transactions = transfer.objects()
    res =  render_template('transactionHistory.html' , transactions = transactions)
    return res
    
       
    




if __name__ == '__main__':
    app.run(debug=True , port=8000)
    
    