from abstracts.LibraryItem import LibraryItem
import uuid
from datetime import datetime
from exceptions.BookNotAvailable import BookNotAvailable

class Book(LibraryItem):

  ALLOWED_STATUSES = {"Available", "Not available", "Locked", "Lost"}

  def __init__(self, title, author, id=None):
    self.title = title
    self.author = author
    self.__id = id or str(uuid.uuid4())
    self.__status = "Available"
    self.holder = None
    self.check_out_date = None

  @property
  def id(self):
      return self.__id

  @id.setter
  def id(self, value):
      return

  @property
  def status(self):
    return self.__status
  
  @status.setter
  def status(self, value):
    if value not in Book.ALLOWED_STATUSES:
      raise ValueError(f"Invalid status: {value}. Allowed: {Book.ALLOWED_STATUSES}")
    self.__status = value

  def __str__(self):
    messages = {
        "Available": f"'{self.title}' by {self.author} is available.",
        "Not available": f"'{self.title}' by {self.author} was checked out on {self.check_out_date} by {self.holder}.",
        "Locked": f"'{self.title}' by {self.author} is a reference book and cannot be checked out."
    }
    # Default fallback if status not recognized
    return messages.get(self.__status, f"'{self.title}' by {self.author} has status {self.__status}.")

  def check_in(self):
    if self.__status == "Not available":
      self.__status = "Available"
      self.holder = self.check_out_date = None


  def check_out(self, member):
    if self.__status == "Available":
      self.__status = "Not available"
      self.holder = member
      self.check_out_date = datetime.today().date()


class ReferenceBook(Book):

  def __init__(self, title, author, id=None):
    super().__init__(title, author, status="Locked")
    self.__id = id or str(uuid.uuid4())

  @property
  def id(self):
      return self.__id

  @id.setter
  def id(self, value):
      return
  
  def __str__(self):
    return "This book is a reference book."
  
  def check_out(self, member):
    raise BookNotAvailable("Reference books cannot be checked out.")