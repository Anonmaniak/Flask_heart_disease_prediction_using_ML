from unicodedata import name
from flask import Flask, render_template, request
from datatrain import predictor
import numpy as np
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form', methods=['GET', 'POST'])
def form(): 
    if request.method == 'GET' : 
        return render_template('form.html')
    age = int(request.form['age'])
    sex = int(request.form['sex'])
    cp = int(request.form['cp'])
    trestbps = int(request.form['trestbps'])
    chol = int(request.form['chol'])
    fbs = int(request.form['fbs'])
    restecg = int(request.form['restecg'])
    thalach = int(request.form['thalach'])
    exang = int(request.form['exang'])
    oldpeak = int(request.form['oldpeak'])
    slope = int(request.form['slope'])
    ca = int(request.form['ca'])
    thal = int(request.form['thal'])
    #output = predictor(np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]))
    output = predictor(np.array([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]).reshape(1, -1))
    print(output)
    if output[0] == 0 : 
        output = 'No heart disease'
    else : 
        output = 'Possibility of heart disease'
    return render_template('form.html', output=output)
if __name__=='__main__':
    app.run(debug=True)