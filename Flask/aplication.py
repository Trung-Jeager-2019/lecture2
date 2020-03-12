from flask import Flask ,render_template,request
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/bye')
def bye():
    headline = "good bye!"
    return render_template("Variable.html", headline = headline)


@app.route('/datetime')
def datetime():
    now = datetime.timezone.now()
    new_year = now.month == 1 and  now.day == 1
    return render_template("New_year.html",new_year = new_year)


@app.route('/name')
def name():
    name = ["Alice", "Bob", "Charlie"]
    return render_template("index.html", name=name)


@app.route('/more')
def more():
    return render_template("more.html",)


@app.route('/layout')
def layout():
    return render_template("layout.html",)


@app.route('/hello',methods=["GET","POST"])
def hello():
    if request.method =="GET":
        return "Please Submit the form instead"
    else:
        name = request.form.get("name")
        return render_template("hello.html",name=name)

# if __name__ == '__main__':
#     app.run()
