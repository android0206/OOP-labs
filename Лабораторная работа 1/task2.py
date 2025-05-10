# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Item, Inventory, Player


if __name__ == "__main__":
    # TODO: инстанцировать все описанные классы, создав три объекта.C()
    item = Item("арбуз", 45, 40)
    inventory = Inventory(100, [item])
    player = Player(100, 100, "Steve", inventory)

    try:
        # TODO: вызвать метод с некорректными аргументами(b)
        item.set_stamina_cost("55")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        # TODO: вызвать метод с некорректными аргументами(a)
        inventory.remove_item("0")
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        # TODO: вызвать метод с некорректными аргументами(a)
        player.sleep("5")
    except TypeError:
        print('Ошибка: неправильные данные')
