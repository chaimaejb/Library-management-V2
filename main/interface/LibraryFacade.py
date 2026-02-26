from interface.UserInterface import UI
from interface.InterfaceManager import IM
from services.MemberService import MemberService
from helper.Membership import Membership
from model.Member import ManagerMembership

class LibraryFacade:
    def __init__(self):
        self.is_connected = False
        self.member = None

    def sign_in(self, username, password):
        member = Membership.is_member(username, password)
        if not member:
            return False
        self.member = member
        self.is_connected = True
        member.show_notifications()
        return True

    def join(self, username, password, membership_type):
        if membership_type != "a" and membership_type != "b":
            print("Membership type not valid!") 
            return
        self.member = MemberService.add_member(username, password, membership_type)
        self.is_connected = True
        return True

        
    def run_member_ui(self):
        if isinstance(self.member.strategy, ManagerMembership):
            IM.run(self.is_connected)
        else:
            UI.run(self.member, self.is_connected)
