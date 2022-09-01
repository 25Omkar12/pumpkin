
from flask import Flask, render_template,request
import pickle
import numpy as np

with open('model.pkl','rb') as f:
    mod = pickle.load(f)

app=Flask(__name__)

@app.route('/')
def trail():
    return render_template('index.html')

@app.route('/pumpkin',methods=["POST"])
def pumpkin():
    A=float(request.form['Area'])
    P=float(request.form['Perimeter'])
    mal=float(request.form['Major_Axis_Length'])
    mil=float(request.form['Minor_Axis_Length'])
    ca=float(request.form['Convex_Area'])
    ed=float(request.form['Equiv_Diameter'])
    E=float(request.form['Eccentricity'])
    S=float(request.form['Solidity'])
    Et=float(request.form['Extent'])
    R=float(request.form['Roundness'])
    Ar=float(request.form['Aspect_Ration'])
    C=float(request.form['Compactness'])
    data = np.array([A, P, mal,mil,ca,ed,E,S,Et,R,Ar,C],ndmin=2)

    result=mod.predict(data)

    print(result)

    return render_template('result.html',type=result[0])

if __name__ == "__main__":
    app.run(host  = '0.0.0.0' , port = 8080 ,debug=False)
