class LibraryCatalog:
  _instance = None

  def __new__(cls):
    if cls._instance == None:
      cls._instance = super().__new__(cls)
      cls._instance.items = []
      cls._instance.members = []
    return cls._instance
  
  def add_item(self, item):
    self.items.append(item)

  def add_member(self, member):
    self.members.append(member)

  def list_items(self):
    return self.items

  def list_members(self):
    return self.members
  
  """
  FOR THE MOMENT IT FEELS HEAVY TO MODIFY MY PROJECT, DO THIS LATER SWEETY <3


  
  Step 1️⃣ Create the Singleton Catalog (NEW FILE)

📁 services/catalog.py

from dataProvider.WriterReader import WriterReader

class LibraryCatalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # ---- Book-related operations ----

    def load_books(self):
        return WriterReader.load_all("Book", "books.json")

    def save_book(self, book):
        WriterReader.save(book, "Book", "books.json")

    def remove_book(self, book):
        WriterReader.remove(book, "books.json")

    # ---- Member operations ----

    def update_member(self, member):
        WriterReader.update(member, "Member", "members.json")


👉 This is your central brain
👉 ONE instance
👉 ONE access point to data

Step 2️⃣ Use Catalog inside BookService (SMALL changes)
Before (your code):
books = WriterReader.load_all("Book", "books.json")

After (only this line changes):
from services.catalog import LibraryCatalog

catalog = LibraryCatalog()
books = catalog.load_books()


That’s it.
No logic changes.

Step 3️⃣ Example: Refactor ONE method together
Original add_book:
@staticmethod
def add_book(title, author):
    book = Book(title, author)
    WriterReader.save(book, "Book", "books.json")

Refactored (safe, minimal):
from services.catalog import LibraryCatalog

@staticmethod
def add_book(title, author):
    book = Book(title, author)
    LibraryCatalog().save_book(book)
  """