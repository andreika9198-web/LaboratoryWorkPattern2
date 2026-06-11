
class PizzaModel:

    def __init__(self, name, price, weight):
        self.__name = name  # название товара/блюда
        self.__price = price  # цена
        self.__weight = weight
        self.__ingredients = []

    @property
    def name(self):
        return self.__name

    @property
    def ingredients(self):
        return self.__ingredients.copy()

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if new_price < 0:
            raise ValueError("Цена не может быть отрицательной")
        if new_price == self.__price:
            raise ValueError('Новая цена совпадает с текущей')

        self.__price = new_price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        if new_weight == self.__weight:
            raise ValueError('Новый вес совпадает с текущей')
        self.__weight = new_weight


    def add_ingredients(self, ingredients):
        self.__ingredients.append(ingredients)


    def delete_ingredients(self,ingredient):
        if len(self.__ingredients) <= 0:
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
        data = {
            'name': self.__name,
            'ingredients': self.__ingredients.copy(),
            'price': self.__price,
            'weight': self.__weight
        }
        return data