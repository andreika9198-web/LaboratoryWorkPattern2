
class PizzaModel:
    """Класс, представляющий модель пиццы с её характеристиками и ингредиентами."""

    def __init__(self, name, price, weight):
        self.__name = name  # название товара/блюда
        self.__price = price  # цена
        self.__weight = weight
        self.__ingredients = []

    @property
    def name(self):
        """Метод для получения название пиццы"""
        return self.__name

    @property
    def ingredients(self):
        """Метод для получения ингредиентов"""
        return self.__ingredients.copy()

    @property
    def price(self):
        """Метод для получения цены пиццы"""
        return self.__price

    @price.setter
    def price(self,new_price):
        """Метод для изменения цены пиццы"""
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if new_price == self.__price:
            raise ValueError('Новая цена совпадает с текущей')

        self.__price = new_price

    @property
    def weight(self):
        """Метод для получения веса пиццы"""
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        """Метод для изменения веса пиццы"""
        if new_weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        if new_weight == self.__weight:
            raise ValueError('Новый вес совпадает с текущим')
        self.__weight = new_weight


    def add_ingredient(self, ingredient):
        """Метод для добавления ингредиента"""
        self.__ingredients.append(ingredient)


    def delete_ingredient(self,ingredient):
        """Метод для удаления ингредиента"""
        if not self.__ingredients:
            raise ValueError('Ингредиентов нет')
        try:
            self.__ingredients.remove(ingredient)
            return True
        except ValueError:
            raise ValueError(f'Ингредиент "{ingredient}" не найден')

    def update_ingredient(self, old_ingredient, new_ingredient):
        """Заменить один ингредиент на другой"""
        try:
            index = self.__ingredients.index(old_ingredient)
            self.__ingredients[index] = new_ingredient
            return True
        except ValueError:
            raise ValueError(f'Ингредиент "{old_ingredient}" не найден')

    def get_pizza(self):
        """Метод возвращает данные о пицце"""
        data = {
            'name': self.__name,
            'ingredients': self.__ingredients.copy(),
            'price': self.__price,
            'weight': self.__weight
        }
        return data