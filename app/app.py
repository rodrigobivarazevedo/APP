from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Create a Flask application instance
app = Flask(__name__)

# Configure the SQLAlchemy database URI, pointing to a SQLite database file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'db', 'database.db')

# Initialize the SQLAlchemy database object
db = SQLAlchemy(app)

# Set a secret key for session management (used for flash messages)
app.secret_key = 'secret_key'

# Define a SQLAlchemy model for the Books table
class Books(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.String(100), nullable=False)
    Author = db.Column(db.String(100), nullable=False)
    Pub_year = db.Column(db.Integer, nullable=False)

# Define a route for the home page that displays the list of books
@app.route('/')
def books():
    # Query all books from the database
    book_list = Books.query.all()

    # Check if there are no books found
    if not book_list:
        book_list = "No books found"

    # Render the 'books.html' template with the book_list data
    return render_template('books.html', book_list=book_list)

# Define a route for adding a new book
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Retrieve form data for the new book
        title = request.form['title']
        author = request.form['author']
        pub_year = request.form['pub_year']

        # Create a new Books object with the form data
        new_book = Books(Title=title, Author=author, Pub_year=pub_year)

        # Add the new book to the database session and commit changes
        db.session.add(new_book)
        db.session.commit()

        # Flash a success message for the user
        flash(f"Added {title} by {author} successfully!", 'success')

        # Redirect to the books route to display the updated list
        return redirect(url_for('books'))

    # If the request method is GET, render the 'add_book.html' template
    return render_template('add_book.html')

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
