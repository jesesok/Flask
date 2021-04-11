from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///new.db'
# db = SQLAlchemy(app)


# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(500), nullable=False)
#     body = db.Column(db.String(500), nullable=False)
#
#     def __repr__(self):
#         return '<Article %r>' % self.id


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
