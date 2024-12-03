# TODO: Подробно описать три произвольных класса
"""
Представлены 3 класса, связанных между собой,
которые описывают какую-то игру, в основном её персонажа и его параметры.
В 3 классах есть различные методы, позволяющие взаимодействовать с их
экземплярами и атрибутами
"""

import doctest


# TODO: описать класс
class Item:
    def __init__(self, name: str, stamina_cost: int = 5, size: int = 1):
        """
        Создание и подготовка к работе объекта класса "Предмет"

        :param name: Название предмета
        :param stamina_cost: Затраченная энергия при использовании
        предмета, по умолчанию равна 5
        :raise ValueError: Если использование предмета не тратит энергию,
        вызываем ошибку
        :param size: Размер предмета, по умолчанию равен 1
        :raise ValueError: Если предмет имеет отрицательный размер
        или не имеет его вовсе, вызываем ошибку

        Примеры:
        Инициализация разных экземпляров класса "Item"
        >>> item_1 = Item("мандарин", 10, 15)
        >>> item_2 = Item("яблоко", 50)
        >>> item_3 = Item("апельсин", size=10)
        """
        if not isinstance(name, str):
            raise TypeError(f"Неподходящий тип данных(not string): {name}")
        self.name = name
        if not isinstance(stamina_cost, int):
            raise TypeError(f"Неподходящий тип данных(not int): {stamina_cost}")
        if stamina_cost <= 0:
            raise ValueError(f"Неподходящее значение(stamina_cost <= 0): {stamina_cost}")
        self.stamina_cost = stamina_cost
        if not isinstance(size, int):
            raise TypeError(f"Неподходящий тип данных(not int): {size}")
        if size <= 0:
            raise ValueError(f"Неподходящее значение(size <= 0): {size}")
        self.size = size

    def rename(self, new_name: str) -> None:
        """
        Метод, который переименовывает предмет

        :param new_name: Новое название предмета

        Примеры:
        >>> item = Item("мандарин", 10, 15)
        >>> item.rename("мандаринка")
        """
        if not isinstance(new_name, str):
            raise TypeError(f"Неподходящий тип данных(not string): {new_name}")
        self.name = new_name

    def set_stamina_cost(self, setted_stamina_cost: int) -> bool:
        """
        Метод, который изменяет/устанавливает значение
        затрачиваемой энергии при использовании предмета

        :param setted_stamina_cost: Устанавливаемое значение
        затрачиваемой энергии
        :return: Изменено ли значение затрачиваемой энергии

        Примеры:
        >>> item_1 = Item("мандарин", 10, 15)
        >>> item_2 = Item("апельсин", size=10)
        >>> item_1.set_stamina_cost(15) # Изменение значения
        Значение изменено
        True
        >>> item_2.set_stamina_cost(25) # Установка значения
        Значение изменено
        True
        """
        if not isinstance(setted_stamina_cost, int):
            raise TypeError(f"Неподходящий тип данных(not int): {setted_stamina_cost}")
        if setted_stamina_cost <= 0:
            print("Недопустимое значение(<= 0)")
            return False
        if setted_stamina_cost > 100:
            print("Недопустимое значение(<= 0)")
            return False
        self.stamina_cost = setted_stamina_cost
        print("Значение изменено")
        return True


# TODO: описать ещё класс
class Inventory:
    def __init__(self, total_size: int, itemlist: list[Item]):
        """
        Создание и подготовка к работе объекта класса "Инвентарь"

        occupied_size : Место в инвентаре, занимаемое предметом

        :param total_size: Общий размер инвентаря
        :param itemlist: Список предметов в инвентаре, в инвентарь
        помещаются объекты класса "Предмет"

        Примеры:
        Инициализация разных экземпляров класса "Inventory"
        >>> item_1 = Item("Апельсин", 19, 20)
        >>> inventory_1 = Inventory(100, [item_1])
        >>> inventory_2 = Inventory(100, [])
        """
        if not isinstance(total_size, int):
            raise TypeError(f"Неподходящий тип данных(not int): {total_size}")
        self.total_size = total_size
        self.occupied_size = 0
        if not isinstance(itemlist, list):
            raise TypeError(f"Неподходящий тип данных(not list): {itemlist}")
        self.items = itemlist
        for item in self.items:
            self.occupied_size += item.size

    def add_item(self, item: Item) -> bool:
        """
        Метод, который добавляет предмет в инвентарь
        (в инвентаре может быть несколько одинаковых предметов)

        :param item: Предмет, который нужно добавить в инвентарь
        :raise ValueError: Если в инвентаре недостаточно места
        для предмета, вызываем ошибку
        :return: True, если предмет добавлен в инвентарь

        Примеры:
        >>> item_ = Item("мандарин", 25, 25)
        >>> inventory_1 = Inventory(100, [])
        >>> inventory_2 = Inventory(100, [item_])
        >>> inventory_1.add_item(item_)  # добавили предмет
        True
        >>> inventory_2.add_item(item_)  # добавили такой же предмет
        True
        """
        if not isinstance(item, Item):
            raise TypeError(f"Неподходящий тип данных(not Item): {item}")
        if self.occupied_size + item.size > self.total_size:
            raise ValueError(f"Инвентарь переполнен")
        self.items.append(item)
        self.occupied_size += item.size
        return True

    def remove_item(self, remove_index: int = 0) -> bool:
        """
        Метод, который убирает предмет из инвентаря

        :param remove_index: Индекс предмета, который нужно убрать,
        по умолчанию равен нулю
        :return: Убран ли предмет из инвентаря

        Примеры:
        >>> item = Item("апельсин", 15, 20)
        >>> inventory_1 = Inventory(100, [item])
        >>> inventory_2 = Inventory(200, [item, item])
        >>> inventory_1.remove_item()  # индекс по умолчанию
        True
        >>> inventory_2.remove_item(1)  # индекс = 1
        True
        >>> inventory_2.remove_item(3)  # индекс = 3(не подходит)
        No index in inventory
        False
        """
        if not isinstance(remove_index, int):
            raise TypeError(f"Неподходящий тип данных(not int): {remove_index}")
        if remove_index < 0:
            if remove_index < -len(self.items):
                print("No index in inventory")
                return False
        if remove_index > len(self.items) - 1:
            print("No index in inventory")
            return False
        self.occupied_size -= self.items[remove_index].size
        self.items.remove(self.items[remove_index])
        return True


# TODO: и ещё один
class Player:
    def __init__(self, hp: int, max_stamina: int, name: str = "Steve", inventory: Inventory = Inventory(100, [])):
        """
        Создание и подготовка к работе объекта класса "Игрок"

        :param hp: Здоровье игрока
        :raise ValueError: Если здоровье игрока меньше или равно нулю,
        вызываем ошибку
        :param max_stamina: Максимальная энергия игрока
        :raise ValueError: Если максимальная энергия игрока меньше нуля,
        вызываем ошибку
        :param name: Имя игрока, по умолчанию: Steve
        :param inventory: Инвентарь игрока, по умолчанию максимальный
        размер инвентаря: 100, инвентарь пуст

        Примеры:
        Инициализация разных экземпляров класса
        >>> item = Item("мандарин", 10, 10)
        >>> player_1 = Player(100, 100, "Android", Inventory(100, [item]))
        >>> player_2 = Player(150, 200)  # со значениями по умолчанию
        """
        if not isinstance(name, str):
            raise TypeError(f"Неподходящий тип данных(not string): {name}")
        self.name = name
        if not isinstance(hp, int):
            raise TypeError(f"Неподходящий тип данных(not int): {hp}")
        if hp <= 0:
            raise ValueError(f"Неподходящее значение(hp < 0): {hp}")
        self.hp = hp
        self.current_hp = hp
        if not isinstance(inventory, Inventory):
            raise TypeError(f"Неподходящий тип данных(not Inventory): {inventory}")
        self.inventory = inventory
        if not isinstance(max_stamina, int):
            raise TypeError(f"Неподходящий тип данных(not int): {max_stamina}")
        if max_stamina < 0:
            raise ValueError(f"Неподходящее значение(stamina < 0): {max_stamina}")
        self.max_stamina = max_stamina
        self.current_stamina = max_stamina

    def use_item(self, index: int = 0) -> bool:
        """
        Метод, с помощью которого игрок использует предмет из инвентаря

        :param index: Индекс предмета, который будет использован,
        по умолчанию равен нулю
        :return: Использован ли предмет

        Примеры:
        >>> item_1 = Item("арбуз", 25, 50)
        >>> item_2 = Item("ананас", 20, 35)
        >>> inventory = Inventory(100, [item_1, item_2])
        >>> player_ = Player(100, 100, "Joe", inventory)
        >>> player_.use_item(1)  # индекс 1
        Item used
        True
        >>> player_.use_item()  # индекс по умолчанию
        Item used
        True
        """
        if not isinstance(index, int):
            raise TypeError(f"Неподходящий тип данных(not int): {index}")
        if index < 0:
            if index < -len(self.inventory.items):
                print("No index in inventory")
                return False
        if len(self.inventory.items) - 1 < index:
            print("No index in inventory")
            return False
        item = self.inventory.items[index]
        if self.current_stamina - item.stamina_cost < 0:
            print("Item not used")
            return False
        self.current_stamina = max(self.current_stamina - item.stamina_cost, 0)
        self.inventory.remove_item(index)
        print("Item used")
        return True

    def sleep(self, hours: int) -> None:
        """
        Метод, который восстанавливает энергию игрока во время сна

        stamina_per_hour - Количество энергии, которая
        восстанавливается за час сна

        :param hours: Количество часов, в течение которых игрок спит
        :ValueError: Если игрок спит меньше одного часа, вызываем ошибку

        Примеры:
        >>> item_ = Item("арбуз", 50, 25)
        >>> player_ = Player(100, 100, "Steve", Inventory(100, [item_]))
        >>> player_.use_item()  # использование предмета(трата энергии)
        Item used
        True
        >>> player_.sleep(2)  # сон(восстановление энергии)
        """
        if not isinstance(hours, int):
            raise TypeError(f"Неподходящий тип данных(not int): {hours}")
        if hours <= 0:
            raise ValueError(f"Неподходящее значение(hours <= 0): {hours}")
        stamina_per_hour = 15
        self.current_stamina = min(self.current_stamina + stamina_per_hour * hours, self.max_stamina)

    def run(self, mins: int) -> None:
        """
        Метод, который расходует энергию игрока во время бега

        stamina_per_minute - Количество энергии, которая
        расходуется за минуту бега

        :param mins: Количество минут, в течение которых игрок бегает
        :raise ValueError: Если время бега меньше одной минуты, вызываем ошибку

        Примеры:
        >>> player_ = Player(100, 100)
        >>> player_.run(5)  # Бег в течение 5 минут
        """
        if not isinstance(mins, int):
            raise TypeError(f"Неподходящий тип данных(not int): {mins}")
        if mins <= 0:
            raise ValueError(f"Неподходящее значение(mins <= 0): {mins}")
        stamina_per_min = 1
        self.current_stamina = max(self.current_stamina - stamina_per_min * mins, 0)

    def check_stats(self) -> None:
        """
        Метод, который позволяет просмотреть параметры игрока

        Получаем параметры: Имя, масимальный размер инвентаря,
        список предметов и место, занимаемое ими, энергия
        и здоровье игрока;
        последний print создаёт отступ, если
        мы захотим несколько раз проверить параметры

        Примеры:
        >>> item_ = Item("ананас", 25, 50)
        >>> player_ = Player(100, 100, "Steve", Inventory(100, [item_]))
        >>> player_.check_stats()  # Вывод параметров игрока
        Name: Steve
        total inventory size: 100
        items:['ананас'], occupied size: 50
        stamina: 100
        hp: 100
        ____________
        """
        print("Name:", self.name)
        print("total inventory size:", self.inventory.total_size)
        print(f"items:{[item.name for item in self.inventory.items]},", "occupied size:", self.inventory.occupied_size)
        print("stamina:", self.current_stamina)
        print("hp:", self.current_hp)
        print("____________")


if __name__ == "__main__":
    doctest.testmod()
