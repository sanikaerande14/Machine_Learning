from flask import Flask, request, jsonify, render_template
import config
from utils import Medical_Insurance
import numpy as np

app=Flask(__name__)
@app.route("/")
def get_home():
    return "Hello Welcome to the ML project. Let's predict the future."

@app.route("/html_page")
def html():
    return render_template("index.html")


@app.route("/predict_charges",methods= ["POST","GET"])
def get_insurance():
    if request.method=="POST":
        data=request.form
        print("User Input Data: ",data)
        age=eval(data["age"])
        gender=data["gender"]
        bmi=eval(data["bmi"])
        children=int(data["children"])
        smoker=data["smoker"]
        region=data["region"]

        med_obj=Medical_Insurance(age,gender,bmi,children,smoker,region)
        charges=med_obj.get_predicted_charges()
        return  jsonify({"Result":f"Predicted Medical Charges are: {charges[0]}"})
    
        
    
if __name__=="__main__":
    
    app.run(debug=True,host=config.HOST_NAME,port=config.PORT_NUMBER)