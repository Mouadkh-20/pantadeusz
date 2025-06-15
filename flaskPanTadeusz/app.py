from flask import Flask, render_template
from markupsafe import Markup

app = Flask(__name__)

# List of books
books = [
    {"number": i, "title": f"Book {i}"} for i in range(1, 13)
]

@app.route('/')
def homepage():
    return render_template("home.html", books=books, active_page='home')

@app.route('/book/<int:book_number>')
def show_book(book_number):
    try:
        filename = f'k{book_number}.html'
        return render_template("book.html", books=books, book_number=book_number, filename=filename, scrollable=True, active_page=f'book{book_number}')
    except Exception as e:
        return f"Error loading book {book_number}: {e}", 404

if __name__ == '__main__':
    app.run(debug=True)