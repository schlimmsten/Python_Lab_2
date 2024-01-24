class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)
        self._pages = 0

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int) -> None:
        if pages > 0 and isinstance(pages, int):
            self._pages = pages
        else:
            print("Incorrect number of pages")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Страниц {self._pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str):
        super().__init__(name, author)
        self._duration = 0

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: int) -> None:
        if duration > 0 and isinstance(duration, float):
            self._duration = duration
        else:
            print("Incorrect number of pages")

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Длительность {self._duration}"


