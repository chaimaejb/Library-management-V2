from model.Member import Member, StudentMembership, PremiumMembership, ManagerMembership, Blocked
from datetime import datetime

class MemberMapper:

  @staticmethod
  def to_dict(obj):
    return {
      "class": obj.__class__.__name__,
      "user": obj.user,
      "password": obj.password.decode("utf-8"),
      "id": obj.id,
      "registration_date": str(obj.registration_date),
      "history": obj.history,
      "borrowing_track": obj.borrowing_track,
      "strategy": obj.strategy.__class__.__name__ if obj.strategy else None
    }

  @staticmethod
  def from_dict(data):
    strategy_map = {
      None: None, 
      "StudentMembership": StudentMembership, 
      "PremiumMembership": PremiumMembership, 
      "ManagerMembership": ManagerMembership,
      "Blocked": Blocked
      }
    
    strategy_cls = strategy_map.get(data.get("strategy"))
    strategy = strategy_cls() if strategy_cls else None
    obj = Member(
      data["user"],
      data["password"].encode("utf-8"),
      strategy,
      data["id"],
      datetime.fromisoformat(data["registration_date"]).date()
    )

    obj.history = data.get("history", [])
    obj.borrowing_track = data.get("borrowing_track", 0)
    return obj