import bcrypt
import uuid
from datetime import datetime
from abstracts.MembershipStrategy import MembershipStrategy
from dataProvider.Notifications import Notifications

class StudentMembership(MembershipStrategy):
  @property
  def max_books(self):
    return 2

  def privileges(self):
    return "Access to student discount and up to 2 borrowed books."

class PremiumMembership(MembershipStrategy):
  @property
  def max_books(self):
    return 10

  def privileges(self):
    return "Access to premium resources and up to 10 borrowed books."

class ManagerMembership(MembershipStrategy):
  @property
  def max_books(self):
    return 20

  def privileges(self):
    return "Full access and management privileges, up to 20 borrowed books."
  
class Blocked(MembershipStrategy):
  @property
  def max_books(self):
    return 0

  def privileges(self):
    return "This member got blocked."

class Member:
  
  def __init__(self, user, password, strategy=None, id=None, registration_date=None):
    self.user = user
    if isinstance(password, str):
      # new member → hash it
      self.__password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    else:
      # loaded member → already hashed
      self.__password = password
    self.__id = id or str(uuid.uuid4())
    self.__registration_date = registration_date if registration_date else datetime.today().date()
    self.history = []
    self.borrowing_track = 0
    self.strategy = strategy
    self.max_books = strategy.max_books if strategy else 1

  @property
  def id(self):
    return self.__id

  @id.setter
  def id(self, value):   #  setters intentionally block changes; but you can acess to the value by calling it by obj._Member.__id =
    return

  @property
  def registration_date(self):
    return self.__registration_date
  @registration_date.setter
  def registration_date(self, value):
    raise ValueError("Can't change this date.")
      
  @property
  def password(self):
    return self.__password
  @password.setter
  def password(self, value):
    if len(value) < 6:
      raise ValueError("Password too weak")

    value = value.encode("utf-8")
    self.__password = bcrypt.hashpw(value, bcrypt.gensalt())

  def show_privileges(self):
    if self.strategy:
      print(f"Membership: {self.strategy.__class__.__name__}")
      print(f"Privileges: {self.strategy.privileges()}")
      print(f"Max books: {self.max_books}")
    else:
      print("No membership strategy assigned.")

  def update(self, turn, book):
    if turn:
      return f"You can borrow {book.title} now! Your reservation will expired within 48h."
    else:
      return f"You're still on the waiting list for the book {book.title}."
  
  def show_notifications(self):
    notifications = Notifications.load_notif()
    if notifications[self.id]:
        print("\n=== Notifications ===")
        for message in notifications[self.id]:
            print(message)


