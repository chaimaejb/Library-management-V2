from dataProvider.WriterReader import WriterReader
from helper.check.Password import Password

class Membership:

  @staticmethod
  def username_exists(user):
    members = WriterReader.load_all("Member", "members.json")
    return any(member.user == user for member in members)

  @staticmethod
  def is_member(user, password):
    members = WriterReader.load_all("Member", "members.json")

    for member in members:
      if member.user == user:
        if Password.check_pw(password, member.password):
          return member 

    return False