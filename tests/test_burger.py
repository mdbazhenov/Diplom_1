import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Bun

class TestBurger:

    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            ('Fluorescent Bun R2-D3', 988.0),
            ('Crater Bun N-200i', 1255.0)
        ]
    )
    def test_set_bun_name(self, burger, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        assert burger.bun.get_name() == bun_name, f"Булочка должна быть {bun_name}"

    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            ('Fluorescent Bun R2-D3', 988.0),
            ('Crater Bun N-200i', 1255.0)
        ]
    )
    def test_set_bun_price(self, burger, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        assert burger.bun.get_price() == bun_price, f"Цена булочки должна быть {bun_price}"

    @pytest.mark.parametrize(
        "ingredient_type, expected_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
            (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142),
        ]
    )
    def test_add_ingredient_type(self, burger, mock_ingredient, ingredient_type, expected_type, expected_name, expected_price):
        ingredient = mock_ingredient(expected_name, expected_price, ingredient_type)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].get_type() == expected_type, f"Тип ингредиента должен быть {expected_type}"

    @pytest.mark.parametrize(
        "ingredient_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
            (INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142),
        ]
    )
    def test_add_ingredient_name(self, burger, mock_ingredient, ingredient_type, expected_name, expected_price):
        ingredient = mock_ingredient(expected_name, expected_price, ingredient_type)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].get_name() == expected_name, f"Имя ингредиента должно быть {expected_name}"

    @pytest.mark.parametrize(
        "ingredient_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
            (INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142),
        ]
    )
    def test_add_ingredient_price(self, burger, mock_ingredient, ingredient_type, expected_name, expected_price):
        ingredient = mock_ingredient(expected_name, expected_price, ingredient_type)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0].get_price() == expected_price, f"Цена ингредиента должна быть {expected_price}"

    @pytest.mark.parametrize(
        "ingredient_type, name, price", [
            (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90),
            (INGREDIENT_TYPE_FILLING, "Сыр с астероидной плесенью", 4142)
        ]
    )
    def test_remove_ingredient(self, burger, mock_ingredient, ingredient_type, name, price):
        ingredient = mock_ingredient(name, price, ingredient_type)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0, "Ингредиент не был удален"

    @pytest.mark.parametrize(
        "ingredient_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
            (INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142),
        ]
    )
    def test_move_ingredient_from_first_to_second(self, burger, mock_ingredient, ingredient_type, expected_name, expected_price):
        ingredient_1 = mock_ingredient(expected_name, expected_price, ingredient_type)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = mock_ingredient('Соус фирменный Space Sauce', 80, INGREDIENT_TYPE_SAUCE)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0].get_name() == 'Соус фирменный Space Sauce', "Первый ингредиент должен быть соусом"

    @pytest.mark.parametrize(
        "ingredient_type, expected_name, expected_price",
        [
            (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
            (INGREDIENT_TYPE_FILLING, 'Сыр с астероидной плесенью', 4142),
        ]
    )
    def test_move_ingredient_to_second_position(self, burger, mock_ingredient, ingredient_type, expected_name, expected_price):
        ingredient_1 = mock_ingredient(expected_name, expected_price, ingredient_type)
        burger.add_ingredient(ingredient_1)
        ingredient_2 = mock_ingredient('Соус фирменный Space Sauce', 80, INGREDIENT_TYPE_SAUCE)
        burger.add_ingredient(ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1].get_name() == expected_name, "Второй ингредиент должен быть"

    @pytest.mark.parametrize(
        "bun_name, bun_price",
        [
            ('Fluorescent Bun R2-D3', 988.0),
            ('Crater Bun N-200i', 1255.0)
        ]
    )
    def test_get_receipt_with_bun_only(self, burger, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        burger.set_buns(bun)
        receipt = burger.get_receipt()
        expected_receipt = (
            f"(==== {bun_name} ====)\n"
            f"(==== {bun_name} ====)\n\n"
            f"Price: {bun_price * 2}"
        )
        assert receipt == expected_receipt, f"Чек должен быть: {expected_receipt}"

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            ('sauce', "Соус Spicy-X", 90),
            ('filling', "Сыр с астероидной плесенью", 4142)
        ]
    )
    def test_get_receipt_with_ingredients(self, burger, mock_ingredient, ingredient_type, name, price):
        ingredient = mock_ingredient(name, price, ingredient_type)
        bun = Bun('Fluorescent Bun R2-D3', 988.0)
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (
            f"(==== {bun.get_name()} ====)\n"
            f"= {ingredient_type.lower()} {name} =\n"
            f"(==== {bun.get_name()} ====)\n\n"
            f"Price: {bun.get_price() * 2 + price}"
        )
        assert receipt == expected_receipt, f"Чек должен быть: {expected_receipt}"







