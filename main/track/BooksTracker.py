from dataProvider.WriterReader import WriterReader

class BooksTracker:

  @staticmethod
  def track_books():
    books = WriterReader.load_all("Book", "books.json")

    available, not_available, locked, lost, other = 0, 0, 0, 0, 0

    for b in books:
      if b.status == "Available":
        available += 1
      elif b.status == "Not available":
        not_available += 1
      elif b.status == "Locked":
        locked += 1
      elif b.status == "Lost":
        lost += 1
      else:
        other += 1

      tracker = {
        "available_books": available,
        "borrowed_books": not_available,
        "reference_books": locked,
        "lost_books": lost,
        "status_undefined": other
        }

    return tracker