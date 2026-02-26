from interface.LibraryFacade import LibraryFacade
from helper.Membership import Membership


class CLI:
    @staticmethod
    def run():
      facade = LibraryFacade()

      while True:
        print("1. Sign in")
        print("2. Join us")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
          attempt = 0
          username = input("Enter your user name: ")
          if not Membership.username_exists(username):
            print("Get your user licence!")
          else:
            while attempt < 4:
              password = input("Enter your password: ")
              if not facade.sign_in(username, password):
                print("Incorrect input!")
                attempt += 1
              else:
                break
            break

        elif choice == "2":
          username = input("Enter your user name: ")
          while not username:
            print("Invalid user name!")
            username = input("Enter your user name: ")
          if Membership.username_exists(username):
            print("User name exists.")
            continue
          password = input("Enter a password: ")
          while len(password) < 6:
            password = input("Password weak, enter at least 6 char: ")
          double_check = input("Re-enter your password for security: ")
          if password == double_check:
            membership = input("Membership type tap 'a' for student membership and 'b' for premium membership: ")
            if facade.join(username, password, membership):
              print("Welcome to our library community!")
              break
          else: 
            print("Passwords not identical")

        elif choice == "3":
          break
        else:

          print("Invalid input!")
          continue

      facade.run_member_ui()
