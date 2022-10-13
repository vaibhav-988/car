from flask import Flask,jsonify,request
import pandas as pd
import numpy as np
import pickle

mod=pickle.load(open('linear.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def welcome():
    return ' welcome to todays session'

@app.route('/prediction')

def prediction():
    current_year=request.form['current_year']	
    Year=request.form['Year']
    Present_Price=request.form['Present_Price']	
    Kms_Driven=request.form['Kms_Driven']

    array=np.array([[current_year,Year,Present_Price,Kms_Driven]])
    test_data=pd.DataFrame(array)

    pred=mod.predict(test_data)
    return jsonify({'my prediction is':pred[0]})

if __name__=='__main__':
    app.run()