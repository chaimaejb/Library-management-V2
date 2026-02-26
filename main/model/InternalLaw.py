class InternalLaw:

  def __init__(self, deadline, late_fee, loss_penalty):
    self.deadline = deadline
    self.late_fee = late_fee
    self.loss_penalty = loss_penalty
  
  def __str__(self):
    return f"The deadline to return books is {self.deadline} days, for each day of delay you gatta pay {self.late_fee} MAD. If you lost or destroyed the book you'll have a penalty of {self.loss_penalty} MAD."

