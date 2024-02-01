from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'db', 'database.db')
db = SQLAlchemy(app)
fake = Faker()

class Books(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Author = db.Column(db.String(100), nullable=False)
    Pub_year = db.Column(db.Integer, nullable=False)

@app.route('/')
def books():
    book_list = Books.query.all()
    return render_template('books.html', books=book_list)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pub_year = request.form['pub_year']

        new_book = Books(Title=title, Author=author, Pub_year=pub_year)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('books'))

    return render_template('add_book.html')



if __name__ == '__main__':
    app.run(debug=True)
