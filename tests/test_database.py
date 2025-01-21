import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    @pytest.mark.parametrize("bun_name, expected_count", [
        ("black bun", 1),
        ("white bun", 1),
        ("red bun", 1)
    ])
    def test_unique_bun_names(self, mock_database, bun_name, expected_count):
        buns = mock_database.available_buns()
        bun_names = [bun.get_name() for bun in buns]

        assert bun_names.count(bun_name) == expected_count, f"Булочка {bun_name} должна быть уникальной."

    @pytest.mark.parametrize("ingredient_name, expected_count", [
        ("hot sauce", 1),
        ("sour cream", 1),
        ("chili sauce", 1),
        ("cutlet", 1),
        ("dinosaur", 1),
        ("sausage", 1)
    ])
    def test_unique_ingredient_names(self, mock_database, ingredient_name, expected_count):
        ingredients = mock_database.available_ingredients()
        ingredient_names = [ingredient.get_name() for ingredient in ingredients]

        assert ingredient_names.count(
            ingredient_name) == expected_count, f"Ингредиент {ingredient_name} должен быть уникальным."

    def test_get_available_buns_count(self, mock_database):
        buns = mock_database.available_buns()
        assert len(buns) == 3, "Количество булочек в базе данных должно быть равно 3."

    def test_get_available_ingredients_count(self, mock_database):
        ingredients = mock_database.available_ingredients()
        assert len(ingredients) == 6, "Количество ингредиентов в базе данных должно быть равно 6."

    @pytest.mark.parametrize("ingredient_type, expected_count", [
        (INGREDIENT_TYPE_SAUCE, 3),
        (INGREDIENT_TYPE_FILLING, 3)
    ])
    def test_get_quantity_of_ingredients_by_type(self, mock_database, ingredient_type, expected_count):
        ingredients = mock_database.available_ingredients()
        filtered_ingredients = [ingredient for ingredient in ingredients if ingredient.get_type() == ingredient_type]

        assert len(
            filtered_ingredients) == expected_count, f"Количество ингредиентов типа {ingredient_type} должно быть {expected_count}."

    @pytest.mark.parametrize("ingredient_name, expected_price", [
        ("hot sauce", 100),
        ("sour cream", 200),
        ("chili sauce", 300),
        ("cutlet", 100),
        ("dinosaur", 200),
        ("sausage", 300)
    ])
    def test_ingredient_price(self, mock_database, ingredient_name, expected_price):
        ingredients = mock_database.available_ingredients()
        ingredient_prices = {ingredient.get_name(): ingredient.get_price() for ingredient in ingredients}

        assert ingredient_prices[
                   ingredient_name] == expected_price, f"Цена для {ingredient_name} должна быть {expected_price}."


