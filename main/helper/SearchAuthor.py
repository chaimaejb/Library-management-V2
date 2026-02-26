from dataProvider.WriterReader import WriterReader

class SearchAuthor:

  @staticmethod
  def with_title(title):
    authors = []
    books = WriterReader.load_all("Book", "books.json")

    for b in books:
      if b.title.casefold() == title.casfold():
        authors.append(b.author)
    return authors
  
  """
  if the author name a member doesnt recognize the author name we ca offer help
  """