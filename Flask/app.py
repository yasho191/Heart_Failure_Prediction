from flask import Flask, render_template,request, redirect
import pickle
import numpy as np
import hashlib


dclf = pickle.load(open('dclf.pkl', 'rb'))
xclf = pickle.load(open('xclf.pkl', 'rb'))
xrclf = pickle.load(open('xrclf.pkl', 'rb'))


app = Flask(__name__)

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

def insert(email, password):
    sql = "INSERT INTO customers (email, password) VALUES (%s, %s)"
    val = (email, password)
    cursor.execute(sql,val)
    db.commit()
    print("record iserted.")

def find(name, password):
    cursor.execute("select * from customers")
    l=cursor.fetchall()
    for i in l:
        if i[0]==name and i[1]==password:
            print("record is present in db")
            return 1
    return 0




"""
import pymysql
db=pymysql.connect(host="database-1.crewf9jbpd79.ap-south-1.rds.amazonaws.com",
        user='yash',
        password='7083581881',
        database="mydb"
        )

cursor=db.cursor()

#cursor.execute('CREATE DATABASE mydb')
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)
#cursor.execute("CREATE TABLE customers (email VARCHAR(255), password VARCHAR(255))")

"""

@app.route('/')
def first_page():
    return render_template('Home.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    #form = MyForm()
    if request.method == 'GET':

        return render_template('signup.html')

    elif  request.method == 'POST':
        # use the form somehow
        # ...
        email = request.form['email']
        password = request.form['password']
        #insert(email,make_hashes(password))
        print('User added successfuly..')
        return redirect('/signin')

@app.route('/signin', methods=['GET','POST'])
def signin():

    if request.method == 'GET':
        return render_template('signin.html')

    if request.form.values() and request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        hashed_pswd = make_hashes(password=password)
        #result = find(email,check_hashes(password,hashed_pswd))
        print('record is created...')

        if result:
            return redirect('/predict')
        else:
            return render_template('signin.html', show="Incorrect Username/Password")

@app.route('/predict',methods=['GET','POST'])
def predict():
    """
    cursor.execute("select * from customers")
    data = cursor.fetchall()
    l = []
    for i in data:
        l.append(i)
    return "you are in predict page {}".format(l)
    """
    if request.method == 'POST' :
        return render_template("PredictionForm.html")

@app.route('/message', methods=['GET',"POST"])
def message():
    """cursor.execute("select * from customers")
    data = cursor.fetchall()
    l = []
    for i in data:
        l.append(i)
    return ' you are in home page {}'.format(l)
    """
    feature1 = int(request.form['Age'])
    feature2 = int(request.form['Gender'])
    feature3 = int(request.form['Anaemia'])
    feature4 = int(request.form['Ejection Fraction'])
    feature5 = int(request.form['Serum Sodium'])
    feature6 = int(request.form['Serum Creatinine'])
    feature7 = int(request.form['Creatinine Phosphokinase'])
    feature8 = int(request.form['Smoking'])
    feature9 = int(request.form['Follow-Up Time'])
    feature10 = int(request.form['Platelets'])
    feature11 = int(request.form['High Blood Pressure'])
    feature12 = int(request.form['Diabetes'])

    arr = np.array(
        [[feature1, feature3, feature7, feature12, feature4, feature11, feature10, feature6, feature5, feature2]])
    print(arr)

    pred1 = dclf.predict(arr)
    pred2 = xrclf.predict(arr)
    pred3 = xclf.predict(arr)

    final_pred = [pred1, pred2, pred3]

    if final_pred.count(1) > final_pred.count(0):
        pred = 1
    else:
        pred = 0

    print(pred)

    return render_template('message.html', data=pred)


if __name__=='__main__':
    app.run()


