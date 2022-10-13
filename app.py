from flask import Flask,request,render_template,url_for
import pandas as pd
import numpy as np
import pickle

mod=pickle.load(open('linear.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/prediction',methods=['POST'])

def prediction():
    current_year=request.form['current_year']	
    Year=request.form['Year']
    Present_Price=request.form['Present_Price']	
    Kms_Driven=request.form['Kms_Driven']

    array=np.array([[current_year,Year,Present_Price,Kms_Driven]])
    test_data=pd.DataFrame(array)

    pred=mod.predict(test_data)
    return render_template('after.html',data=pred[0])

if __name__=='__main__':
    app.run()