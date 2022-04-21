########################################################################################
######################          Import packages      ###################################
########################################################################################
from operator import ge
from flask import Blueprint, render_template, flash, request, Markup
from flask_login import login_required, current_user
import numpy as np
import pandas as pd
from __init__ import create_app, db
import pickle
from predictPage import scaler, genderconversion, familyconversion, benefitconversion, careconversion, leaveconversion, anonymconversion, workconversion
from chatbotPage import tfidf, faq
from suggestion import suggestion
########################################################################################
# our main blueprint

model = pickle.load(open('model.pkl', 'rb'))
chatbotModel = pickle.load(open('chatbot.pkl', 'rb'))

main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def home():
    # if(current_user.name == )
    print(current_user)
    return render_template('home.html')

@main.route('/predict',methods=['POST','GET'])
def predictPage():
    return render_template('index.html', name=current_user.name)

@main.route('/prediction',methods=['POST','GET'])
def predict():
    if request.method=='POST':
        age = request.form.get('Age')
        gender = request.form['gender']
        family_history = request.form['family_history']
        benefits = request.form['benefits']
        care_options = request.form['care_options']
        leave = request.form['leave']
        anonymity = request.form['anonymity']
        work_interference = request.form['work_interference']
        print(age, gender,family_history, benefits, care_options,leave,anonymity,work_interference)
        fitted_age = scaler.transform(np.array([[age]]))
        arr = np.array([[fitted_age, gender, family_history, benefits, care_options, leave, anonymity, work_interference]])
        data = model.predict(arr)
        pred = ""
        prob = ""
        if(data[0] == 0):
            pred = "NO"
            prob = "doesn't require any"
        else:
            pred = "YES"
            prob = "requires"
        gend = genderconversion(gender)
        family = familyconversion(family_history)
        benefit = benefitconversion(benefits)
        care = careconversion(care_options)
        leav = leaveconversion(leave)
        anonym = anonymconversion(anonymity)
        work = workconversion(work_interference)
        print(gend, family,benefit,care,leav,anonym,work)
        sugg = suggestion(int(age))
        sugg = Markup(sugg)
        pred= Markup('<strong>{} !!!!!, <br> Your Mental Health Condition {} treatment.</strong>'.format(pred,prob))
        print(age, gend,family, benefit, care, leav, anonym, work, pred, sugg)
        return render_template('predict.html', **locals())

@main.route('/resources',methods=['POST','GET'])
def resourcePage():
    return render_template('resources.html', name=current_user.name)

@main.route('/help',methods=['POST','GET'])
def helpPage():
    return render_template('document.html', name=current_user.name)

@main.route('/about',methods=['POST','GET'])
def aboutPage():
    return render_template('about.html', name=current_user.name)

@main.route('/explore',methods=['POST','GET'])
def explorePage():
    return render_template('explore.html', name=current_user.name)

@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/chatbot',methods=['POST','GET'])
def chatbot():
    return render_template('chatbot.html', name=current_user.name)

@main.route('/get',methods=['POST','GET'])
def getBotResponse():
    search_test = [request.args.get('msg')]
    search_engine = tfidf.transform(search_test)
    pred = chatbotModel.predict(search_engine)
    data=""
    for question in pred:
        faq_data = faq.loc[faq.isin([question]).any(axis=1)]
        data = faq_data['Answers'].values
    res = str(data)[1:-1]
    res = res.replace('\\n','<br>')
    return res


app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode