from flask import Flask,jsonify,render_template,redirect,request,url_for
import config
from utility import ConStrength

app=Flask(__name__)

@app.route('/predict_strength',methods=['GET','POST'])

def prediction():
    if request.method=='POST':
        data=request.form
        print('data',data)

        conc_str= ConStrength(data)
        con_strength=conc_str.predict_strength()
        print('::::::',con_strength)
        return jsonify({'concret strength :':con_strength})

if __name__=='__main__':
    app.run()