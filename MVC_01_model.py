
class PizzaModel:

    def __init__(self, name, price, weight):
        self.__name = name  # название товара/блюда
        self.__price = price  # цена
        self.__weight = weight
        self.__ingredients = []

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,new_price):
        if new_price < 0:
            raise ValueError("цена не может быть отрицательным")
        if new_price == self.__price:
            raise ValueError('Новая цена совпадает с текущей')
        if new_price < self.__price:
            raise ValueError('Новая цена не может быть меньше старой')
        self.__price = new_price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        if new_weight < 0:
            raise ValueError("цена не может быть отрицательным")
        if new_weight == self.__price:
            raise ValueError('Новая цена совпадает с текущей')
        self.__weight = new_weight


    def add_ingredients(self, ingredients):
        self.__ingredients.append(ingredients)


    def change_ingredients(self,ingredient):
        if len(self.__ingredients) <= 0:
            raise ValueError('Ингридиентов нету')
        try:
            self.__ingredients.remove(ingredient)
            return True
        except ValueError:
            return 'Такого ингридиента нету'


    def get_pizza(self):
        data = {
            'name': self.__name,
            'ingredients': self.__ingredients,
            'price': self.__price,
            'weight': self.__weight
        }
        return data