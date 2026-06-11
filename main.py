from MVC_02_view import PizzaView, PizzaController

if __name__ == '__main__':
    """Функция для демонстрации работы MVC для Пиццы"""

    print("=" * 50)
    print("ДОБРО ПОЖАЛОВАТЬ В ПИЦЦЕРИЮ")
    print("=" * 50)

    # 1. Создаем пиццу "Маргарита"
    print("\n--- СОЗДАНИЕ ПИЦЦЫ ---")
    controller = PizzaController("Маргарита", 450, 400)
    view = PizzaView(controller)

    # 2. Добавляем ингредиенты
    print("\n--- ДОБАВЛЕНИЕ ИНГРЕДИЕНТОВ ---")
    view.add_ingredient("тесто")
    view.add_ingredient("томатный соус")
    view.add_ingredient("моцарелла")
    view.add_ingredient("базилик")

    # 3. Показываем полную информацию
    print("\n--- ИНФОРМАЦИЯ О ПИЦЦЕ ---")
    view.display_all()

    # 4. Показываем только состав и вес
    print("\n--- СОСТАВ И ВЕС ---")
    view.display_consist()

    # 5. Показываем только цену
    print("\n--- ЦЕНА ---")
    view.display_price()

    # 6. Изменяем цену
    print("\n--- ИЗМЕНЕНИЕ ЦЕНЫ ---")
    view.update_price(520)
    view.display_price()

    # 7. Изменяем вес
    print("\n--- ИЗМЕНЕНИЕ ВЕСА ---")
    view.update_weight(450)
    view.display_consist()

    # 8. Добавляем новый ингредиент
    print("\n--- ДОБАВЛЕНИЕ ИНГРЕДИЕНТА ---")
    view.add_ingredient("орегано")
    view.display_consist()

    # 9. Заменяем ингредиент
    print("\n--- ЗАМЕНА ИНГРЕДИЕНТА ---")
    view.update_ingredient("базилик", "петрушка")
    view.display_consist()

    # 10. Удаляем ингредиент
    print("\n--- УДАЛЕНИЕ ИНГРЕДИЕНТА ---")
    view.delete_ingredient("орегано")
    view.display_consist()

    # 11. Финальная информация
    print("\n--- ФИНАЛЬНАЯ ИНФОРМАЦИЯ ---")
    view.display_all()

    print("\n" + "=" * 50)
    print("СПАСИБО ЗА ПОСЕЩЕНИЕ ПИЦЦЕРИИ!")
    print("=" * 50)