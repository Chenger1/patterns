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
    counter = 0

    def __init__(self, format_name: str):
        self.format_name = format_name
        self._increase_counter()

    @classmethod
    def _increase_counter(cls):
        cls.counter += 1

    def open_reader(self, book: Book):
        return f'Open {book.title}. {book.author} with format {self.format_name}'


def library():
    formats = ('pdf', 'fb2', 'epub', 'djvu', 'docx', 'txt')
    books = []
    for elem in range(500000):
        form = random.choice(formats)
        created_format = Format(form)
        book = Book(title=f'Title-{elem}',
                    author=f'Author-{elem}',
                    book_format=created_format)
        books.append(book)
    print(books[1000].open_reader())
    print(f'Books: {len(books)}')
    print(f'Formats: {Format.counter}')


if __name__ == '__main__':
    tracemalloc.start()
    library()
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10 ** 6}MB; Peak was {peak / 10 ** 6}MB")
    tracemalloc.stop()
