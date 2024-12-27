"""
Представлен класс Game, описывающий какой-то шутер и унаследованный от него класс CS2. В классе CS2 унаследованы
защищённые атрибуты name, mode, hp и свойства name, mode. Перегружен метод hp.setter и магический метод __repr__ и
добавлен новый атрибут serv и метод serv_setter_by_index.
"""

SERVERS_LIST = ["Frankfurt", "Amsterdam", "Helsinki", "Berlin", "Moscow"]  # Список серверов
MODES_LIST = ["Matchmaking", "Deathmatch", "Wingman", "Premier", "Casual"]  # Список режимов игры


class Game:
    def __init__(self, name: str, mode: int, hp: int):
        """
        Создание и подготовка к работе объекта базового класса "Game"

        :param name: Название игры
        :raise TypeError: Название игры может быть только строкой
        :param mode: Индекс режима игры, который устанавливает режим из списка MODES_LIST с помощью метода
         mode_setter_by_index()
        :raise TypeError: Индекс может быть только целым числом
        :param hp: hp в игре
        :raise TypeError: hp может быть только целым числом
        :raise ValueError: hp не может быть меньше или равно нулю
        """
        if not isinstance(name, str):
            raise TypeError("Неверный тип данных, должен быть str")
        self._name = name  # Атрибут защищённый и неизменяемый, название игры не может быть изменено
        if not isinstance(mode, int):
            raise TypeError("Неверный тип данных, должен быть int")
        self._mode = None  # Атрибут защищённый, пользователь сможет поменять режим игры только через специальный метод
        self.mode_setter_by_index(mode)
        if not isinstance(hp, int):
            raise TypeError("Неверный тип данных, должен быть int")
        if hp <= 0:
            raise ValueError("Неподходящее значение, должно быть больше нуля")
        self._hp = hp  # Атрибут защищённый, hp устанавливает/меняет разработчик; метода для пользователя нет

    @property
    def name(self) -> str:
        """
        Свойство атрибута name

        :return: Возвращается защищённый атрибут name
        """
        return self._name

    @property
    def mode(self) -> str:
        """
        Свойство атрибута mode

        :return: Возвращается защищённый атрибут mode
        """
        return self._mode

    @property
    def hp(self) -> int:
        """
        Свойство атрибута hp

        :return: Возвращается защищённый атрибут hp
        """
        return self._hp

    @hp.setter
    def hp(self, new_hp: int) -> None:
        """
        Setter для hp(для разработчика)

        :param new_hp: Новое устанавливаемое значение hp
        :raise ValueError: Значение должно быть больше нуля
        """
        if not isinstance(new_hp, int):
            raise TypeError("Неверный тип данных, должен быть int")
        if new_hp <= 0:
            raise ValueError("Неподходящее значение, должно быть больше нуля")
        self._hp = new_hp

    def mode_setter_by_index(self, mode_index: int) -> None:
        """
        Метод, устанавливающий режим игры по индексу из списка MODES_LIST(для пользователей)

        :param mode_index: Индекс режима игры
        :raise TypeError: Индекс может быть только целым числом
        :raise ValueError: Индекс не может выходить за пределы списка
        """
        if not isinstance(mode_index, int):
            raise TypeError("Неверный тип данных, должен быть int")
        if mode_index < 0:
            raise ValueError("Неподходящий индекс, должен быть не меньше нуля")
        if mode_index >= len(MODES_LIST):
            raise ValueError("Индекса нет в списке")
        self._mode = MODES_LIST[mode_index]

    def __str__(self) -> str:
        """
        Магический метод __str__

        :return: Возвращается простая строка для пользователя, описывающая созданный экземпляр класса
        """
        return f'Игра "{self.name}" типа "{self.mode}"'

    def __repr__(self) -> str:
        """
        Магический метод __repr__

        :return: Возвращается строка, показывающая, как может быть инициализирован экземпляр
        """
        return f"{self.__class__.__name__}(name={self.name!r}, mode={self.mode!r}, hp={self.hp})"


class CS2(Game):
    def __init__(self, name: str, mode: int, serv: int, hp: int = 100):
        """
        Создание и подготовка к работе объекта дочернего класса "CS2", расширен конструктор базового класса - добавлен
        атрибут serv, так же добавлен метод serv_setter_by_index(), унаследован метод mode_setter_by_index() и
        магический метод __str__, перегружен метод hp.setter и __repr__

        :param serv: Индекс сервера, который устанавливает сервер из списка SERVERS_LIST с помощью метода
         serv_setter_by_index()
        """
        super().__init__(name, mode, hp)
        self._serv = None  # Атрибут защищённый, пользователь сможет поменять сервер только через специальный метод
        self.serv_setter_by_index(serv)

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, new_hp: int) -> None:
        """
        Перегруженный setter для hp(для разработчика). Перегружаем метод, т.к. добавляется условие - конкретно в этом
        классе максимальное значение hp - 100, но может быть от 0 до 100 для различных кастомных игр

        :raise ValueError: в данном классе hp не может быть больше 100
        """
        if not isinstance(new_hp, int):
            raise TypeError("Неверный тип данных, должен быть int")
        if new_hp > 100:
            raise ValueError("Неподходящее значение, должно быть не больше ста")
        self._hp = new_hp

    @property
    def serv(self) -> None:
        return self._serv

    def serv_setter_by_index(self, serv_index: int) -> None:
        """
        Метод, устанавливающий сервер для игры по индексу из списка SERVERS_LIST(для пользователей)

        :param serv_index: Индекс сервера
        :raise TypeError: Индекс может быть только целым числом
        :raise ValueError: Индекс не может выходить за пределы списка
        """
        if not isinstance(serv_index, int):
            raise TypeError("Неверный тип данных, должен быть int")
        if serv_index < 0:
            raise ValueError("Неподходящий индекс, должен быть не меньше нуля")
        if serv_index >= len(SERVERS_LIST):
            raise ValueError("Индекса нет в списке")
        self._serv = SERVERS_LIST[serv_index]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, mode={self.mode!r}, serv={self.serv!r}, hp={self.hp})"
