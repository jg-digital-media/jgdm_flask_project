# import flask class
from flask import Flask
from flask import render_template

# use whatever the current namespace is as instance name
app = Flask (__name__)  

# multi routes
@app.route('/')
@app.route('/<name>')
def hello(name="Castle Eden, Durham."):
     return render_template("index.html", name=name)


# Flask Routing
@app.route('/photos')
def photos():
    return render_template("photos.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/tutorial')
@app.route('/tutorials')
def tutorial():
    return render_template("tutorials/tutorial.html")


@app.route('/tutorials/2')
def tutorial_page_2():
    return render_template("tutorials/tutorial-two.html")


@app.route('/tutorials/3')
def tutorial_page_3():
    return render_template("tutorials/tutorial-three.html")


@app.route('/tutorials/4')
def tutorial_page_4():
    return render_template("tutorials/tutorial-four.html")






# return a html string
def add(num1, num2):
    return render_template("multiply.html", num1=num1, num2=num2)

# app.run(debug=True, port=8000, host='0.0.0.0')
