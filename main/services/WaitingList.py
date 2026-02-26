from dataProvider.WaitingListData import WaitingListData

class WaitingList:
  waiting_list = WaitingListData.load_queue()

  @staticmethod
  def attach(member, book):
    if member not in WaitingList.waiting_list[book.id]:
      WaitingList.waiting_list[book.id].append(member.id)
      WaitingListData.save_queue(WaitingList.waiting_list)

  @staticmethod
  def detach(member, book):
    if member in WaitingList.waiting_list[book.id]:
      WaitingList.waiting_list[book.id].remove(member.id)
      WaitingListData.save_queue(WaitingList.waiting_list)

  @staticmethod
  def get_next_member(book):
    if WaitingList.waiting_list[book.id]:
      next_member = WaitingList.waiting_list[book.id].pop(0)
      WaitingListData.save_queue(WaitingList.waiting_list)
      return next_member
    return None
  
  @staticmethod
  def show_waiting_list(book):
    """Display the current waiting list for a specific book."""
    return WaitingList.waiting_list[book.id]
  
