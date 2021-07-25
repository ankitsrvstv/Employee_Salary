from logging import debug
from flask import Flask , render_template ,request
import salary as s


app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def hello(mk=0):
    if request.method=="POST":
        years=request.form['years']
        salary_pred=s.salary_prediction(years)
        mk=salary_pred
        
    
    return render_template("index.html",my_salary= mk)


"""
@app.route("/sub" , methods=['POST'])
def submit():
    if request.method=="POST":
        name=request.form["username"]
    return render_template("sub.html", n = name)    
"""


if __name__=="__main__":
    app.run(debug=True)
