from flask import Flask, render_template,request
app=Flask (__name__) 
import pickle
import joblib 
model=pickle.load(open(r'rdf.pkl','rb'))


@app.route('/')
def hello():

 return render_template("index.html")
@app.route('/guest', methods = [ "POST"])
def Guest():
 senl=request.form["sen1"]
 sen2=request.form["sen2"] 
 sen3=request.form[ "sen3"]
 sen4=request.form[ "sen4"]
 sen5=request.form[ "sen5"]
 sen6=request.form["sen6"]

@app.route('/y_predict', methods = ["POST"]) 
def y_predict():

 x_test = [[(yo) for yo in request.form.values()]]

 prediction=model.predict(x_test)

 prediction = prediction[0]

 return render_template("secondpage.html",y=prediction)
app.run(debug=True)