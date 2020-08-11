from flask import Flask,request,render_template
import pickle
app=Flask(__name__)


@app.route('/',methods=['GET'])
def home():

    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def pred():

    preg = float(request.form['pregnancies'])
    glucose = float(request.form['glucose'])
    bp = float(request.form['bloodpressure'])
    skin = float(request.form['skin'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    dmf = float(request.form['dmf'])
    age = float(request.form['age'])


    with open('Di.pickle','rb') as f:
        Model=pickle.load(f)


    prediction=Model.predict([[preg,glucose,bp,skin,insulin,bmi,dmf,age]])[0]

    if prediction==0:

        return render_template('results.html',prediction="Congrats!! ,You are NON DIABETIC")

    else:

        return render_template('results.html',prediction="You are DIABETIC, You need to take care")




if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app

