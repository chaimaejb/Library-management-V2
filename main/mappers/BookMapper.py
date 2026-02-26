from model.Book import Book, ReferenceBook
from datetime import datetime
from mappers.MemberMapper import MemberMapper

class BookMapper:

  @staticmethod
  def to_dict(obj):
    return {
      "class": obj.__class__.__name__,
      "title": obj.title,
      "id": obj.id,
      "author": obj.author,
      "status": obj.status,
      "holder": MemberMapper.to_dict(obj.holder) if obj.holder else None,
      "check_out_date": str(obj.check_out_date) if obj.check_out_date else None
    }
  
  @staticmethod
  def from_dict(data):
    cls_map = {"Book": Book, "ReferenceBook": ReferenceBook}
    klass = cls_map[data["class"]]
    obj = klass(data["title"], data["author"], data["id"])
    if data["class"] == "Book":   
      obj.status = data["status"]
      if data["check_out_date"]:
        obj.holder = MemberMapper.from_dict(data["holder"]) if data["holder"] else None
        obj.check_out_date = datetime.fromisoformat(data["check_out_date"]).date()
    elif data["class"] == "ReferenceBook":
      obj.status = data["status"]
    return obj