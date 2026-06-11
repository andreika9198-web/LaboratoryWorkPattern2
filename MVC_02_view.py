from MVC_03_controller import PizzaController

class PizzaView:
    def __init__(self, controller: PizzaController):
        """Класс-представление для отображения информации о пицце. Отвечает за взаимодействие с пользователем."""
        self.controller = controller

    def update_price(self, new_price):
        """ Метод для отображения результата изменения цены."""
        result = self.controller.update_price(new_price)
        if result is False:
            print(f'Введены не корректные данные - {new_price}')
        elif result is True:
            print(f'Цена была успешно изменена на {new_price}')
        else:
            print(f'Ошибка {result}')

    def update_weight(self, new_weight):
        """Метод для отображения результата изменения веса."""
        result = self.controller.update_weight(new_weight)
        if result is False:
            print(f'Введены не корректные данные - {new_weight}')
        elif result is True:
            print(f'Вес был успешно изменен на {new_weight}')
        else:
            print(f'Ошибка {result}')

    def add_ingredient(self, ingredient):
        """Метод для отображения результата добавления ингредиента."""
        result = self.controller.add_ingredient(ingredient)
        if result is False:
            print(f'Введены не корректные данные - {ingredient}')
        else:
            print(f'Ингредиент был успешно добавлен - {ingredient}')

    def delete_ingredient(self, ingredient):
        """ Метод для отображения результата удаления ингредиента."""
        result = self.controller.delete_ingredient(ingredient)
        if result is False:
            print(f'Введены не корректные данные - {ingredient}')
        elif result is True:
            print(f'Ингредиент был успешно удален - {ingredient}')
        else:
            print(f'Ошибка {result}')

    def update_ingredient(self, old_ingredient, new_ingredient):
        """ Метод для отображения результата замены ингредиента."""
        result = self.controller.update_ingredient(old_ingredient, new_ingredient)
        if result is False:
            print(f'Введены не корректные данные')
        elif result is True:
            print(f'Ингредиент {old_ingredient} был успешно изменен на {new_ingredient}')
        else:
            print(f'Ошибка {result}')

    def display_all(self):
        """Метод для отображения полной информации о пицце.
        Показывает: название, состав, вес и цену."""
        result = self.controller.get_pizza()
        print(result['name'])
        print(f'Состав пиццы: ')
        for item in result['ingredients']:
            print(f'  -{item}')
        print(f'Вес пиццы - {result["weight"]}')
        print(40 * '=')
        print(f'Цена - {result["price"]}')
        print(40 * '=')

    def display_consist(self):
        """ Метод для отображения состава и веса пиццы.
        Показывает: список ингредиентов и вес."""
        result = self.controller.get_pizza()
        print(f'Состав пиццы: ')
        for item in result['ingredients']:
            print(f'  -{item}')
        print(f'Вес пиццы - {result["weight"]}')
        print(40 * '=')

    def display_price(self):
        """Метод для отображения только цены пиццы."""
        result = self.controller.price()
        print(40 * '=')
        print(f'Цена - {result}')
        print(40 * '=')
