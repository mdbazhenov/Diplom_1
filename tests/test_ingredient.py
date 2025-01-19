import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Тесты на класс Ingredient
class TestIngredient:
    # Проверка корректного сохранения типа ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "горячий соус", 100), (INGREDIENT_TYPE_FILLING, "сыр", 70), ], )
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    # Проверка корректного сохранения имени ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "горячий соус", 100), (INGREDIENT_TYPE_FILLING, "сыр", 70), ], )
    def test_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # Проверка корректного сохранения цены ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "горячий соус", 100), (INGREDIENT_TYPE_FILLING, "сыр", 70), ], )
    def test_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
