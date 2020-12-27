from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///base.db"
database = SQLAlchemy(app)


class Article(database.Model):
    id = database.Column(database.Integer, primery_key=True)
    title = database.Column(database.String(100), nullable=False)
    intro = database.Column(database.String(300), nullable=False)
    text = database.Column(database.Text, nullable=False)
    date = database.Column(database.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return  '<Article %r>' % self.id


@app.route('/home')
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return f"user page: {name} - {id}..."


if __name__ == '__main__':
    app.run(debug=True)
