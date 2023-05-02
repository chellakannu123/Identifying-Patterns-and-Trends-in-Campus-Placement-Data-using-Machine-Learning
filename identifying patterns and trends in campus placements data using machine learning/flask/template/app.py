<section id="hero" class="d-flex flex-column justify-content-center">
  <div class="container"> 
    <div class="row justify-content-center">
      <div class="col-xl-8">
    <h1>Identifying patterens and trends in campus placement data using machine learning</h1>
  </div>
 </div>
</div>
</section><!-- End Hero -->
<section id="about" class="about">
 <div class="container">
   <div class="section-title">
    <h2>Fill the details</h2>
</div>
  <div class="row content">
    <form action="{{ url_for('y_predict')}}" method="POST">
        <input type="number" id="sen1" name="sen1" placeholder="Age"> 
        <input type="number" id="sen2" name="sen2" placeholder="Gender M(0), F(0)">
        <input type="number" id="sen3" name="sen3" placeholder="Stream CS(0), IT(1), ECE (2), Mech(3), EEE (4), Civil 
        <input type="number" id="sen4" name="sen4" placeholder="Internships"> 
        <input type="number" id="sen5" name="sen5" placeholder="CGPA">
        <input type="number" id="sen6" name="sen6" placeholder="number of backlogs">
        <input type="submit" value="submit">
     </form>
   </div>
  </div>
 </div>
</section><!-- end about us section -->
|<section_id="hero" class="d-flex flex-column justify-content-center">
  <div class="container">
   <div class="row justify-content-center"> 
    <div class="col-xl-8">
   <h1>The Prediction is: {{y}}</h1>
   <h3>> represents Not-Placed </h3>
   <h3> 1 represents Placed<h2>
   </div>
  </div>
 </div>
</section><!-- End Hero -->
from flask import Flask, render_template, request
app=Flask(___name___)
import pickle 
import joblib
model=pickle.load(open("placement123.pkl", 'rb')) 
ct=joblib.load('placement')
@app.route('/')
def hello():
    return render_template("index.html")
@app.route('/guest', methods = ["POST"])
def Guest():
    sen1=request.form["sen1"]
    sen2=request.form["sen2"]
    sen3=request.form["sen3"]
    sen4=request.form["sen4"]
    sen5=request.form["sen5"]
    sen6=request.form["sen6"]
@app.route('/y_predict', methods = ["POST"]) 
def y_predict():
    x_test = [[(yo) for yo in request.form.values()]]
    prediction -model.predict(x_test)
    prediction = prediction[0]
    return render_template("secondpage.html",y=prediction)
app.run(debug=True)       