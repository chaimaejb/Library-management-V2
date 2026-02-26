from track.BooksTracker import BooksTracker
from dataProvider.WriterReader import WriterReader
from dataProvider.InternalLawData import InternalLawData
from dataProvider.Notifications import Notifications
from services.BookService import BookService
from services.MemberService import MemberService

class IM:     # in large project with many managers should control who makes changes

  @staticmethod
  def run(is_connected):
     while is_connected:
        print("=== Menu ===") 
        print("1. Add a book")  # CHECKED
        print("2. Remove a book")  # CHECKED
        print("3. Track books")  # CHECKED
        print("4. Display members")  # CHECKED
        print("5. Display books")  # CHECKED
        print("6. Block member")  # CHECKED
        print("7. Modify law")  # CHECKED
        print("8. Exit ")

        choice = input("Enter your choice: ")

        if choice == "1":
          title = input("Enter the title you want to add: ")
          author = input("Enter author's name: ")

          BookService.add_book(title, author)
        
        elif choice == "2":
          title = input("Enter the title you want to remove: ")
          author = input("Enter author's name: ")

          BookService.remove_book(title, author)
        
        elif choice == "3":
          tracker = BooksTracker.track_books()
          print(tracker)

        elif choice == "4":
          members = WriterReader.load_all("Member", "members.json")
          for mem in members:
            print("user name: ",mem.user,"/ id: ", mem.id,"/ ", mem.history, mem.borrowing_track, mem.strategy.__class__.__name__)
        
        elif choice == "5":
          books = WriterReader.load_all("Book", "books.json")
          for b in books:
            print("title: ", b.title,"/ author: ", b.author,"/ id: ", b.id,"/ status: ", b.status,"/ borrowed by: ", b.holder.user if b.holder else b.holder,"/ check out date: ", b.check_out_date)

        elif choice == "6":
          member_id = input("Which member do you want to block, enter his id: ")
          MemberService.block_member(member_id)

        elif choice == "7":
          allowed_arg = {"deadline", "late fee", "loss penalty"}
          print("Allowed arg to choose: ", allowed_arg)
          rule = input("Enter what you want to modify: ")

          new_rule = input("Enter the new rule: ") 

          InternalLaw = InternalLawData.load_rules()

          if rule == "deadline":
            InternalLaw.deadline = int(new_rule)
          elif rule == "late fee":
            InternalLaw.late_fee = float(new_rule)
          elif rule == "loss penalty":
            InternalLaw.loss_penalty = float(new_rule)
          else:
            print("Invalid input!")
            break
          InternalLawData.save_rules(InternalLaw)
          print("Rules changed succesfully.")
          members = WriterReader.load_all("Member", "members.json")
          for mem in members:
            Notifications.add_notif(mem.id, "We updated our rules, please check them out!")

        elif choice == "8":
          is_connected = False
          
          from interface.CLI import CLI
          CLI.run()

        else:
          print("Incorrect input.")
          continue