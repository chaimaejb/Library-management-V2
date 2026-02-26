import json
from collections import defaultdict
from datetime import datetime

class Next:

    FILE = "data/nextMember.json"

    @staticmethod
    def save(data):
        with open(Next.FILE, "w") as f:
            json.dump(data, f)

    @staticmethod
    def up_to_borrow(member_id, book_id):
        first = Next.load()
        first[book_id] = {
                "member_id": member_id,
                "notified_at": datetime.now().isoformat(),
                "time_limit_hours": 48
            } 
        Next.save(first)
    @staticmethod
    def load():
        try:
            with open(Next.FILE, "r") as f:
                data = json.load(f)
                return defaultdict(dict, data) 
        except FileNotFoundError:
            return defaultdict(dict)


