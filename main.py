import json

from flask import Flask, render_template

app = Flask(__name__)

books = [
    {
        'id': 1,
        'titre': 'un titre',
    },
    {
        'id': 2,
        'titre': 'un autre titre random',
    },
    {
        "id": 3,
        "titre": "a"
    }
]

file = open('books.json')
books = json.load(file)["books"]


@app.route("/")
def index():
    return render_template("home.html")


def get_book_by_id(id):
    book = filter(lambda book_element: str(book_element["id"]) == str(id), books)
    result = next(book, None)
    if result is None:
        return False
    else:
        return result


def get_book_by_title(title):
    book = filter(lambda book_element: book_element["titre"] == title, books)
    result = next(book, None)
    if result is None:
        return False
    else:
        return result


@app.route("/books/id/<id>", methods=["GET"])
def by_id(id):
    return show_result(get_book_by_id(id))


@app.route("/books/titre/<title>", methods=["GET"])
def by_title(title):
    return show_result(get_book_by_title(title))


def show_result(searched_book):
    return render_template("result.html", book=searched_book)


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
