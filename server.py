from flask import *

import numpy

import pandas as pd

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier


app=Flask(__name__)


#Student Placement Prediction
@app.route('/')
def student():
  return render_template("placement.html")

@app.route('/stud_plac',methods=["POST"])
def student1():
  Age=eval(request.form.get("age"))
  Gender=int(request.form.get("gender"))
  Stream=int(request.form.get("stream"))
  Internship=int(request.form.get("internship"))
  Hostel=int(request.form.get("hostel"))
  Cgpa=eval(request.form.get("cgpa"))
  Backlog=int(request.form.get("backlog"))
  
  url="collegePlacement_cleanData.csv"
  data=pd.read_csv(url)
  data=data.values
  x=data[:,:-2]
  y=data[:,-1]
  
  model=DecisionTreeClassifier()
  model.fit(x,y)
  
  z=model.predict([[Age,Gender,Stream,Internship,Hostel,Cgpa,Backlog]])
  
  return render_template("placement.html",data=z[0])

if __name__ == '__main__':
  app.run()