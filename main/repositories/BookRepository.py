from mappers.BookMapper import BookMapper
from dataProvider.WriterReader import WriterReader

class BookRepository:

    def get_all(self):
        data = WriterReader.read("books.json") 
        return [BookMapper.from_dict(d) for d in data]

    def get_by_id(self, book_id):
        books = self.get_all()
        book = next((b for b in books if b.id == book_id), None)
        return book

    def get_by_part_book_title(self, part_of_title):
        books = self.get_all()
        search_list = {}
        for b in books:
            title = b.title.strip().lower()
            if part_of_title in title:
                if b.author not in search_list:
                    search_list[b.author] = set()
                search_list[b.author].add(b.title)
        return search_list
    
    def get_by_title_and_author(self, title, author):
        books = self.get_all()
        book = next((b for b in books if b.title.casefold() == title.casefold() and b.author.casefold() == author.casefold()), None)
        return book

    def save(self, book):
        data = WriterReader.read("books.json")     
        data.append(BookMapper.to_dict(book))
        
        WriterReader.write("books.json", data)

    def update(self, book):
        data = WriterReader.read("books.json")
        for i, d in enumerate(data):
            if d["id"] == book.id:
                data[i] = BookMapper.to_dict(book)
                break
        WriterReader.write("books.json", data)

    def delete(self, book):
        data = WriterReader.read("books.json")
        for i, d in enumerate(data):
            if d["id"] == book.id:
                del data[i]
                break
        WriterReader.write("books.json", data)