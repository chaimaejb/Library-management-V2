import json
from collections import defaultdict
from datetime import datetime

class Notifications:

    FILE = "data/notifications.json"

    @staticmethod
    def save_notif(notifications):
        with open(Notifications.FILE, "w") as f:
            json.dump(notifications, f)
            
    @staticmethod
    def add_notif(member_id, notification):
        notifications = Notifications.load_notif()
        member_notifications = notifications[member_id]
        if len(member_notifications) >= 4 :
            member_notifications.pop(0)
        member_notifications.append(datetime.now().isoformat() + " - " + notification) 
        Notifications.save_notif(notifications)     
        
    @staticmethod
    def clear_notif(member_id):
        notifications = Notifications.load_notif()
        notifications[member_id] = []
        Notifications.save_notif(notifications) 

    @staticmethod
    def load_notif():
        try:
            with open(Notifications.FILE, "r") as f:
                data = json.load(f)
                return defaultdict(list, data) 
        except FileNotFoundError:
            return defaultdict(list)

