from mappers.MemberMapper import MemberMapper
from model.DVD import DVD
from datetime import datetime

class DVDMapper:

  @staticmethod
  def to_dict(obj):
    return {
      "class": obj.__class__.__name__,
      "title": obj.title,
      "director": obj.director,
      "duration": obj.duration,
      "id": obj.id,
      "status": obj.status,
      "holder": MemberMapper.to_dict(obj.holder),
      "check_out_date": str(obj.check_out_date)
    }

  @staticmethod
  def from_dict(data):
    cls_map = {"DVD": DVD}
    klass = cls_map[data["class"]]
    obj = klass(data["title"], data["director"], data["duration"], data["id"])
    obj.status = data["status"]
    if data["check_out_date"]:
      obj.holder = MemberMapper.from_dict(data["holder"])
      obj.check_out_date = datetime.fromisoformat(data["check_out_date"]).date()
    return obj