from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql///newdb'


@app.route('/')
def hello_world():
    return render_template("name.html")


@app.route('/abs')
def plas():
    a = 4
    b = 4
    return str(a + b)


if __name__ == '__main__':
    app.run()
