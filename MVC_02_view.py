from MVC_03_controller import PizzaController

class PizzaView:
    def __init__(self, controller: PizzaController):
        self.controller = controller

    def update_price(self, new_price):
        result = self.controller.update_price(new_price)
        if result is False:
            print(f'Введены не корректные данные - {new_price}')
        elif result is True:
            print(f'Цена была успешно изменена на {new_price}')
        else:
            print(f'Ошибка {result}')

    def update_weight(self, new_weight):
        result = self.controller.update_price(new_weight)
        if result is False:
            print(f'Введены не корректные данные - {new_weight}')
        elif result is True:
            print(f'Вес был успешно изменен на {new_weight}')
        else:
            print(f'Ошибка {result}')

    def add_ingredient(self, ingredient):
        result = self.controller.add_ingredient(ingredient)
        if result is False:
            print(f'Введены не корректные данные - {ingredient}')
        else:
            print(f'Ингредиент был успешно добавлен - {ingredient}')

    def delete_ingredient(self, ingredient):
        result = self.controller.delete_ingredient(ingredient)
        if result is False:
            print(f'Введены не корректные данные - {ingredient}')
        elif result is True:
            print(f'Ингредиент был успешно удален - {ingredient}')
        else:
            print(f'Ошибка {result}')

    def update_ingredient(self, old_ingredient, new_ingredient):
        result = self.controller.update_ingredient(old_ingredient, new_ingredient)
        if result is False:
            print(f'Введены не корректные данные')
        elif result is True:
            print(f'Ингредиент {old_ingredient} был успешно изменен на {new_ingredient}')
        else:
            print(f'Ошибка {result}')


