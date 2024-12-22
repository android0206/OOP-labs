class Book:
    """ Базовый класс книги. В классе имеется проверка для атрибутов, которые в дальнейшем нельзя будет изменить."""

    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Неподходящий тип данных")
        self._name = name
        if not isinstance(author, str):
            raise TypeError("Неподходящий тип данных")
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self) -> str:
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
    Дочерний класс бумажной книги, унаследованный от базового класса. Предполагается, что изначально разработчик знает
    какие значения могут принимать атрибуты и создаёт экземпляры класса с верными значениями. Проверки созданы
    только для стороннего пользователя, который в дальнейшем сможет изменить значение pages.
    """

    def __init__(self, name: str, author: str, pages: int = None):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Неподходящий тип данных")
        if new_pages <= 0:
            raise ValueError("Неподходящее значение")
        self._pages = new_pages

    def __str__(self) -> str:
        return f"Бумажная книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """
    Дочерний класс аудиокниги, унаследованный от базового класса. Предполагается, что изначально разработчик знает
    какие значения могут принимать атрибуты и создаёт экземпляры класса с верными значениями. Проверки созданы
    только для стороннего пользователя, который в дальнейшем сможет изменить значение duration.
    """

    def __init__(self, name: str, author: str, duration: float = None):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_value: float) -> None:
        if not isinstance(new_value, float):
            raise TypeError("Неподходящий тип данных")
        if new_value <= 0:
            raise ValueError("Неподходящее значение")
        self._duration = new_value

    def __str__(self) -> str:
        return f"Аудиокнига {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
