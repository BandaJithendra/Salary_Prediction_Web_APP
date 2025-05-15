
from flask import Flask, render_template,request, redirect,url_for
import pickle
import numpy as np
from currencies import Currency
cur = Currency('INR')



app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def Login():
    x = request.form['exprience']
    if x=='' or x.isdigit()==False or int(x)>50:
        return redirect(url_for('home'))
    x = int(x)
    res = int(model.predict([[x]]))
    # res = locale.currency(res)
    # res = cur.get_money_format(res)
    return render_template('login.html',ans = res)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001,debug=True)
