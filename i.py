from flask import Flask,jsonify,render_template,redirect,request,url_for
import config
from utility import ConStrength

app=Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome to Concrete Strength Prediction")
    return render_template("index1.html")

@app.route('/predict_strength',methods=['GET','POST'])
def get_con_strength():

    if request.method=='POST':
        data=request.form
        print('data',data)

        conc_str= ConStrength(data)
        con_strength=conc_str.predict_strength()
        return render_template("index1.html", prediction = con_strength)
    
    else:
        data=request.form
        print('data',data)

        conc_str= ConStrength(data)
        con_strength=conc_str.predict_strength()
        return render_template("index1.html", prediction = con_strength)
        
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080,debug=False)