from abstracts.LibraryItem import LibraryItem
import uuid
from datetime import datetime

class DVD(LibraryItem):

  ALLOWED_STATUSES = {"Available", "Not available", "Lost", "Damaged"}

  def __init__(self, title, director, duration, id=None):
    self.title = title
    self.director = director
    self.duration = duration
    self.id = id or str(uuid.uuid4())
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
    if value not in DVD.ALLOWED_STATUSES:
      raise ValueError(f"Invalid status: {value}. Allowed: {DVD.ALLOWED_STATUSES}")
    self.__status = value

  def __str__(self):
    return f"DVD '{self.title}' directed by {self.director} ({self.duration} min) — Status: {self.__status}"
  
  def check_in(self):
    if self.__status == "Not available":
      self.__status = "Available"
      self.holder = self.check_out_date = None

      from dataProvider.WriterReader import WriterReader
      WriterReader.update(self, "DVD", "DVD.json")

  def check_out(self, member):
    if self.__status == "Available":
      self.__status = "Not available"
      self.holder = member
      self.check_out_date = datetime.today().date()

      from dataProvider.WriterReader import WriterReader
      WriterReader.update(self, "DVD", "DVD.json")
