from model.Member import Member, StudentMembership, PremiumMembership, Blocked
from dataProvider.WriterReader import WriterReader
from dataProvider.Notifications import Notifications
from dataProvider.NextMember import Next
from services.WaitingList import WaitingList
from datetime import datetime, timedelta

class MemberService:

  @staticmethod
  def add_member(user, password, membership):
    membership_map = {
      "a": StudentMembership(),
      "b": PremiumMembership()
    }
    strategy = membership_map[membership]
    if not strategy:
      raise ValueError("Invalid membership type")
    member = Member(user, password, strategy)
    WriterReader.save(member, "Member", "members.json")
    return member
  
  @staticmethod
  def block_member(id):
    members = WriterReader.load_all("Member", "members.json")
    member = next((m for m in members if m.id == id), None)
    if not member:
      raise ValueError("Member not found!")
    member.strategy = Blocked()
    WriterReader.update(member, "Member", "members.json")
    print(f"Member {member.user} has been blocked.")
  
  @staticmethod
  def change_pw(member, new_password):
    member.password = new_password
    from dataProvider.WriterReader import WriterReader
    WriterReader.update(member, "Member", "members.json")

  @staticmethod
  def notify_next_member(book_id):
    books = WriterReader.load_all("Book", "books.json")
    members = WriterReader.load_all("Member", "members.json")
    book = next((b for b in books if b.id == book_id), None)
    if not book:
      return None
    first = WaitingList.get_next_member(book)
    if first:
      next_member = next((m for m in members if m.id == first), None)
      Next.up_to_borrow(first, book.id)
      message = next_member.update(True, book)
      Notifications.add_notif(first, message)
      return next_member.id
    return None
  
  @staticmethod
  def update_queue():
    expired_reservation = []
    now = datetime.now()
    queue = Next.load()
    for book_id, info in queue.items():
      if now - datetime.fromisoformat(info["notified_at"]) > timedelta(hours=48):
        Notifications.add_notif(info["member_id"], f"Reservation expired for book {book_id}, moving to next member...")
        expired_reservation.append(book_id)
    for book_id in expired_reservation:
        del queue[book_id]
    if expired_reservation:
        Next.save(queue)
    for book_id in expired_reservation:
        MemberService.notify_next_member(book_id)
        

