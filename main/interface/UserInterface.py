from services.BookService import BookService
from services.MemberService import MemberService
from helper.BooksByAuthor import BooksByAuthor
from helper.SearchAuthor import SearchAuthor
from dataProvider.WriterReader import WriterReader
from dataProvider.InternalLawData import InternalLawData
from dataProvider.Notifications import Notifications
from model.InternalLaw import InternalLaw
from helper.check.Password import Password

class UI:

  rules = InternalLawData.load_rules()

  @staticmethod
  def run(member, is_connected):
    while is_connected:
      print("=== Menu ===")
      print("1. Check in a book")  # CHECKED
      print("2. Check out a book")  # CHECKED
      print("3. End membership")  # CHECKED
      print("4. Show books list")  # CHECKED
      print("5. Discover our internal law")  #CHECKED
      print("6. Change password")  # CHECKED
      print("7. Report lost book")  # CHECKED
      print("8. Clear notifications") #  CHECKED
      print("9. Log out")

      choice = input("Enter your choice: ")

      if choice == "1":
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        BookService.check_in(title, author, member)

      elif choice == "2":
        title = input("What book do you want, Enter the title: ")
        author = input("Enter the author, (if you don't have his name type '0' so we can help): ")

        if author == "0":
          authors = SearchAuthor.with_title(title)
          if not authors:
            print("Book not found!")
            continue
          print("This is the list of authors: ", authors)
          print("Type '2' to relaunch your request.")
          continue

        BookService.check_out(title, author, member)

      elif choice == "3":
        validation = input("When you end your membership you lose access to our services. Are you sure you want to end it? Press '0' to confirm, else press any othor button.")
        if validation == "0":
          if member.borrowing_track != 0:
            print("We can't end your membership until you return the borrowing books.")
          else:
            WriterReader.remove(member, "members.json")
            print("We ended your membership.")
            is_connected = False
            from interface.CLI import CLI
            CLI.run()

      elif choice == "4":
        books_list = BooksByAuthor.rebuild()
        print("This is a list of available books in our library: ", books_list)

      elif choice == "5":
        print(UI.rules)

      elif choice == "6":
        password = input("For security, enter your current password: ")
        pass_changed = False
        
        if Password.check_pw(password, member.password):
          while not pass_changed:
            pass1 = input("Enter your new password, at least 6 characters: ")
            pass2 = input("Re-write your new password: ")
            if pass1 == pass2 and len(pass1) >= 6:
              MemberService.change_pw(member, pass1)
              pass_changed = True
              print("Your password changed succesfully.")
            else:
              print("Passwords not identical or weak!")
        else :
          print("Password incorrect!")

      elif choice == "7":
        title = input("Enter the book title: ")
        author = input("Enter author name: ")

        if BookService.mark_lost(member, title, author):
          print(f"Following our internal law, we ask you to pay a penalty of {UI.rules.loss_penalty} MAD.")
        else:
          print("Book not found!")

      elif choice == "8":
        Notifications.clear_notif(member.id)

      elif choice == "9":
        is_connected = False

        from interface.CLI import CLI
        CLI.run()

      else: 
        print("Incorrect input!")
