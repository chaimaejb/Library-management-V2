from abc import ABC, abstractmethod

class MembershipStrategy(ABC):
    
  @property
  @abstractmethod
  def max_books(self):
    """Return the maximum number of books the member can borrow."""
    pass

  @abstractmethod
  def privileges(self):
    """Return a short description of privileges."""
    pass
