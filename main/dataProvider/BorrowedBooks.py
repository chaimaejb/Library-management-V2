import json
from collections import defaultdict

class Borrowed:

    FILE = "data/borrowedBooks.json"

    @staticmethod
    def save(data):
        with open(Borrowed.FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def take(member_id, book_id):
        borrowed_list = Borrowed.load()
        borrowed_list[member_id].append(book_id)      
        Borrowed.save(borrowed_list)
    @staticmethod
    def turn(member_id, book_id):
        borrowed_list = Borrowed.load()
        if book_id in borrowed_list[member_id]:
            borrowed_list[member_id].remove(book_id)      
            Borrowed.save(borrowed_list)
    @staticmethod
    def load():
        try:
            with open(Borrowed.FILE, "r") as f:
                data = json.load(f)
                return defaultdict(list, data) 
        except FileNotFoundError:
            return defaultdict(list)

