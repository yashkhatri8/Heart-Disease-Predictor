from flask import Flask,render_template,request,url_for
app=Flask(__name__)
import numpy as np

import pickle

filename='heart-Disease-prediction.pkl'
prediction=pickle.load(open(filename,'rb'))

@app.route('/')
@app.route('/main')
def home():
    return render_template("main.html")


@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/predict")
def predict():
    return render_template("prediction.html")


@app.route("/result",methods=['POST'])
def result():
    age=int(request.form['age'])
    gender = int(request.form['sex'])
    cp = int(request.form['cp'])
    restbp = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs= int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])
    predictData=np.array([[age,gender,cp,restbp,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    result=prediction.predict(predictData)
    print(result)
    return render_template("result.html",output=result)








if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
