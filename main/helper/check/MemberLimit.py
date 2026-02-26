class MemberLimit:

  @staticmethod
  def can_borrow(member):
    """
    Returns True if the member can borrow more books,
    i.e., they haven't reached their maximum borrowing limit.
    """
    return member.borrowing_track < member.max_books
  