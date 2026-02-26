from collections import defaultdict
from dataProvider.WriterReader import WriterReader

class BooksByAuthor:

  @staticmethod
  def rebuild(filename="books.json", only_available=True):  # If you want to seperate available book by author ONLY_AVAILABLE is true by default, otherwise you can give it false to build all books
    books_by_author = defaultdict(list)
    for book in WriterReader.load_all("Book", filename):
      if not only_available or book.status == "Available":
        books_by_author[book.author].append(book.title)
    return books_by_author

