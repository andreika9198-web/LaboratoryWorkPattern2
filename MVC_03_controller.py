from  MVC_01_model import PizzaModel

class PizzaController:
    """Класс-контроллер для управления пиццей. Выступает посредником между Model и View."""
    def __init__(self, name, price, weight):
        self.model = PizzaModel(name, price, weight)

    def price(self):
        """Метод для получения цены пиццы"""
        return self.model.price

    def update_price(self, new_price):
        """Метод для изменения цены пиццы."""
        if not isinstance(new_price, (int,float)):
            return False
        try:
            self.model.price = new_price
            return True
        except ValueError as e:
            return str(e)


    def update_weight(self, new_weight):
        """Метод для изменения веса пиццы."""
        if not isinstance(new_weight, (int,float)):
            return False
        try:
            self.model.weight = new_weight
            return True
        except ValueError as e:
            return str(e)

    def add_ingredient(self, ingredient):
        """Метод для добавления ингредиента."""
        if not isinstance(ingredient, str)  or not ingredient.strip():
            return False
        self.model.add_ingredient(ingredient)
        return True

    def delete_ingredient(self, ingredient):
        """Метод для удаления ингредиента."""
        if not isinstance(ingredient, str):
            return False
        try:
            self.model.delete_ingredient(ingredient)
            return True
        except ValueError as e:
            return  str(e)

    def update_ingredient(self, old_ingredient, new_ingredient):
        """Метод для замены одного ингредиента на другой"""
        if not isinstance(old_ingredient, str) or not isinstance(new_ingredient,str):
            return False
        try:
            self.model.update_ingredient(old_ingredient, new_ingredient)
            return True
        except ValueError as e:
            return str(e)

    def get_pizza(self):
        """Метод для получения данных о пицце"""
        return self.model.get_pizza()