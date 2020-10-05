from flask import *
import time as t
a=Flask(__name__)
akl=True
@a.route('/')
def hp():
    return render_template("now.html")
@a.route('/calculator',methods=["POST","GET"])
def hpq():
    if request.method=="POST":
        try:
            k=f"Result  {eval(request.form['expression'])}"
        except NameError:
            k="invalid expression"
        
    
        return redirect(url_for("hpr",name2=k))
    else:
        return render_template("par2.html")
@a.route('/<name2>')
def hpr(name2):
    return name2
if __name__ == "__main__":

    a.run(debug=True)