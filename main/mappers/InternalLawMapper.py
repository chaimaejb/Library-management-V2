from model.InternalLaw import InternalLaw

class InternalLawMapper:

  @staticmethod
  def to_dict(obj):
    return {
      "class": obj.__class__.__name__,
      "deadline": obj.deadline,
      "late_fee": obj.late_fee,
      "loss_penalty": obj.loss_penalty,
    }
  
  @staticmethod
  def from_dict(data):
    obj = InternalLaw(data["deadline"], data["late_fee"], data["loss_penalty"])
    return obj