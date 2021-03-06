import random
import tracemalloc


class Book:
    def __init__(self, title: str, author: str, book_format: 'Format'):
        self.title = title
        self.author = author
        self.book_format = book_format

    def open_reader(self):
        return self.book_format.open_reader(self)


class Format:
    def __init__(self, format_name: str):
        self.format_name = format_name

    def open_reader(self, book: Book):
        return f'Open {book.title}. {book.author} with format {self.format_name}'


def library():
    formats = ('pdf', 'fb2', 'epub', 'djvu', 'docx', 'txt')
    books = []
    created_formats = set()
    for elem in range(500000):
        form = random.choice(formats)
        created_format = Format(form)
        created_formats.add(created_format)
        book = Book(title=f'Title-{elem}',
                    author=f'Author-{elem}',
                    book_format=created_format)
        books.append(book)
    print(books[1000].open_reader())
    print(f'Books: {len(books)}')
    print(f'Formats: {len(created_formats)}')


if __name__ == '__main__':
    tracemalloc.start()
    library()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
    tracemalloc.stop()
