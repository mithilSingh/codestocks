from flask import*
app=Flask(__name__)
app.route("/")
def hp():
    return render_template("clint.html")
if __name__=="__main__":
    app.run(debug=True)