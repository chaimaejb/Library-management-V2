import json
from collections import defaultdict

class WaitingListData:

    FILE = "data/waitingList.json"
    
    @staticmethod
    def save_queue(waiting_list):
        with open(WaitingListData.FILE, "w") as f:
            json.dump(waiting_list, f)
    @staticmethod
    def load_queue():
        try:
            with open(WaitingListData.FILE, "r") as f:
                data = json.load(f)
                return defaultdict(list, data) 
        except FileNotFoundError:
            return defaultdict(list)

