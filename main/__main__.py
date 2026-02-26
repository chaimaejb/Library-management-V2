from interface.CLI import CLI
from services.MemberService import MemberService

if __name__ == "__main__":
    MemberService.update_queue()
    CLI().run()