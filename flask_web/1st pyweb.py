from flask import *
import time as t
a=Flask(__name__)
akl=True
ans=""
@a.route('/')
def hp():
    return render_template("now.html")
@a.route('/calculator',methods=["POST","GET"])
def hpq():
    if request.method=="POST":
        try:
            k=f"{eval(request.form['expression'])}"
        except :
            k="invalid expression"
        
    
        return render_template("par2.html",a=k)
    else:
        return render_template("par2.html")

if __name__ == "__main__":

    a.run(debug=True)