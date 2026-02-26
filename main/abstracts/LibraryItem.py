from abc import ABC, abstractmethod

class LibraryItem(ABC):
  @property
  @abstractmethod
  def id(self):
    pass
  @property
  def status(self):
    pass
  
  @abstractmethod
  def check_in(self):
    pass
  @abstractmethod
  def check_out(self, member):
    pass


"""
@property means: Access this method like an attribute, not like a function.
@abstarctmethod : forced customization; Every subclass MUST implement this itself.
Non-abstract property (like status) : shared behavior

✔ Every LibraryItem MUST have:
  - id
  - check_in()
  - check_out()

✔ status exists
  - but the base class may define it
  - subclasses may inherit it
"""