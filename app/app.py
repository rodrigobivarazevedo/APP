from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'db', 'database.db')
db = SQLAlchemy(app)
fake = Faker()

app.secret_key = 'secret_key'

class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    First_name = db.Column(db.String(50), nullable=False)
    Last_name = db.Column(db.String(50), nullable=False)
    Email = db.Column(db.String(120), unique=True, nullable=False)
    Role = db.Column(db.String(50), nullable=False, default='user')  


@app.route('/')
def index():
    users = Users.query.all()
    if not users:
        users = "No users found"
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        Firstname = request.form['firstname']
        Lastname = request.form['lastname']
        Email = request.form['email']
        

        new_user = Users(First_name=Firstname, Last_name=Lastname, Email=Email)
        db.session.add(new_user)
        db.session.commit()
        flash(f"Added {Firstname} {Lastname} successfully!", 'success')
        return redirect(url_for('index'))

    return render_template('add_user.html')

@app.route('/generate_fake_users')
def generate_fake_users():
    for _ in range(2):
        fake_firstname = fake.first_name()
        fake_lastname = fake.last_name()
        fake_email = fake.email()
        

        new_fake_user = Users(First_name=fake_firstname, Last_name=fake_lastname, Email=fake_email)
        db.session.add(new_fake_user)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
