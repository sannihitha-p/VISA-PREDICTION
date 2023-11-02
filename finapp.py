# -*- coding: utf-8 -*-
"""
Created on Mon April 26 17:03:46 2021

@author: Pinka
"""

from flask import Flask,render_template,request
import pickle
import numpy as np
model=pickle.load(open(r"C:/Users/hp/Desktop/Batch-10 Visa Approval Prediction/flask/dtc2.pkl",'rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("fin.html")
@app.route('/login',methods=['POST'])
def login():
    file=request.form['ap']
    if(file=="Y"):
        s1=1
    if(file=="N"):
        s1=0
    file1=request.form['ag']
    file2=request.form['bp']
    file3=request.form['subday']
    file4=request.form['submonth']
    file5=request.form['subyear']
    file6=request.form['decday']
    file7=request.form['decyear']
    file8=request.form['decmonth']
    
    total=[[int(file3),int(file4),int(file5),int(file6),int(file8),int(file7),s1,int(file1),int(file2)]]
    y_pred=[]
    y_pred = [[3]]
  
    y_pred=model.predict(np.array(total))

    
    if (y_pred==[[0]]):
        return render_template("fin.html",showcase=" Your VISA is DENIED  ")
        
    if(y_pred==[[1]]):
         return render_template("fin.html",showcase="Your VISA is CERTIFIED WITHDRAWN")
    if(y_pred==[[2]]):
         return render_template("fin.html",showcase="Your VISA is CERTIFIED")
    else:
         return render_template("fin.html",showcase="Your VISA is WITHDRAWN")
    
if(__name__)=='__main__':
     app.run(debug=False)