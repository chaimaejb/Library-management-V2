from repositories.BookRepository import BookRepository
from dataProvider.WriterReader import WriterReader
from dataProvider.InternalLawData import InternalLawData
from dataProvider.BorrowedBooks import Borrowed
from dataProvider.NextMember import Next
from exceptions.BookNotAvailable import BookNotAvailable
from helper.check.MemberLimit import MemberLimit
from datetime import datetime
from model.Book import Book
from model.InternalLaw import InternalLaw
from services.WaitingList import WaitingList
from services.MemberService import MemberService

class BookService:

  rules = InternalLawData.load_rules()
  book_repository = BookRepository()

  @staticmethod
  def add_book(title, author):

    book_exist = BookService.book_repository.get_by_title_and_author(title, author)
    if book_exist:
      print("This book is already in our library")
      return
    book = Book(title, author)
    BookService.book_repository.save(book)
    print("Book added succesfully.")
  
  @staticmethod
  def remove_book(title, author):
    book = BookService.book_repository.get_by_title_and_author(title, author)
    if not book:
      raise ValueError ("Book not found!")
    if book.status == "Not available":
      print("This book is already borrowed! try another time.")
      return 
    BookService.book_repository.delete(book)
    print("Book removed succesfully.")

  @staticmethod
  def add_to_history(member, book):
    record = {
      "book_id": book.id,
      "checkout_date": datetime.now().isoformat(),
      "checkin_date" : None,
      "status": "borrowed"
    }
    member.history.append(record)
    member.borrowing_track += 1
    WriterReader.update(member, "Member", "members.json")

  @staticmethod
  def mark_return(member, book):
    for record in reversed(member.history): 
      if record["book_id"] == book.id and record["checkin_date"] is None:
        record["checkin_date"] = datetime.now().isoformat()
        record["status"] = "returned"
        member.borrowing_track -= 1
        WriterReader.update(member, "Member", "members.json")
        break

  @staticmethod
  def mark_lost(member, title, author):
    book = BookService.book_repository.get_by_title_and_author(title, author)
    if not book:
      return False
    for record in reversed(member.history):
      if record["book_id"] == book.id and record["status"] == "borrowed":
        record["status"] = "lost"
        book.status = "Lost"
        WriterReader.update(member, "Member", "members.json")
        BookService.book_repository.update(book)
        member.borrowing_track -= 1
        return True

  @staticmethod
  def check_in(title, author, member):
  #  members = WriterReader.load_all("Member", "members.json")
    borrowed_books = Borrowed.load()
    by_user = borrowed_books[member.id]

    book = BookService.book_repository.get_by_title_and_author(title, author)
    if not book or book.id not in by_user:
      print("You never borrowed this book!")
      return
        
    if book.status == "Not available":
      today = datetime.today().date()
      borrowed_days = (today - book.check_out_date).days

      if borrowed_days > BookService.rules.deadline:
        overdue_days = borrowed_days - BookService.rules.deadline
        penalty = overdue_days * BookService.rules.late_fee
        print(f"Overdue by {overdue_days} days. Penalty: {penalty} MAD.")

      print(f"Thank you for returning {book.title}! See you soon.")
      book.check_in()
      BookService.book_repository.update(book)
      BookService.mark_return(member, book)
      Borrowed.turn(member.id, book.id)
      MemberService.notify_next_member(book.id)

    else:
      print(f"{book.title} is already available in the library!")

  
  @staticmethod
  def check_out(title, author, member):
    if not MemberLimit.can_borrow(member):
      print("You've acheived your limit!")
      return

    book = BookService.book_repository.get_by_title_and_author(title, author)
    if not book:
      raise ValueError ("Book not found!")

    if book.status == "Locked":
      raise BookNotAvailable("This book can't be checked out.")
    
    elif book.status == "Not available":
      if member.id not in WaitingList.waiting_list[book.id] and book.holder.id != member.id:
        WaitingList.attach(member, book)
        print("The book is not available for the moment, you're on the waiting list")

    elif book.status == "Available":
      queue = Next.load()
      reservation = queue.get(book.id)
      if not reservation:
        book.check_out(member)
        BookService.book_repository.update(book)
        BookService.add_to_history(member, book)
        Borrowed.take(member.id, book.id)
        print("Have a nice lecture!")
      elif reservation and reservation["member_id"] == member.id:
        book.check_out(member)
        BookService.book_repository.update(book)
        BookService.add_to_history(member, book)
        Borrowed.take(member.id, book.id)
        del queue[book.id]
        Next.save(queue)
        print("Have a nice lecture!")
      elif member.id not in WaitingList.waiting_list[book.id]:
        WaitingList.attach(member, book)
        print("The book is reserved, you're on the waiting list")
        
    else:
      raise BookNotAvailable("Sorry, this book not available for the moment! wanna look for another title?")
