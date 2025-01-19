import pytest
from unittest.mock import MagicMock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.burger import Burger
from praktikum.database import Database


# Фикстура для создания ингредиента
@pytest.fixture
def mock_ingredient():
    """
    Фикстура для создания мока ингредиента.
    Используется для создания мока ингредиента с указанными свойствами.

    Пример использования:
        ingredient = mock_ingredient("Соус Spicy-X", 90, INGREDIENT_TYPE_SAUCE)
    """

    def _mock_ingredient(name, price, ingredient_type):
        # Создаем мок для ингредиента с заданными значениями
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        mock_ingredient.get_type.return_value = ingredient_type
        return mock_ingredient

    return _mock_ingredient


# Фикстура для создания бургера
@pytest.fixture
def burger():
    """
    Фикстура для создания объекта бургера.
    """
    return Burger()


# Фикстура для базы данных
@pytest.fixture
def database():
    """Фикстура для создания экземпляра базы данных."""
    return Database()


# Фикстура для мокированных булочек
@pytest.fixture
def mock_buns():
    """Фикстура для мокированных булочек."""
    return [
        MagicMock(name="black bun", get_name=MagicMock(return_value="black bun")),
        MagicMock(name="white bun", get_name=MagicMock(return_value="white bun")),
        MagicMock(name="red bun", get_name=MagicMock(return_value="red bun"))
    ]


# Фикстура для мокированных ингредиентов
@pytest.fixture
def mock_ingredients():
    """Фикстура для мокированных ингредиентов."""
    return [
        MagicMock(get_name=MagicMock(return_value="hot sauce"), get_type=MagicMock(return_value=INGREDIENT_TYPE_SAUCE), get_price=MagicMock(return_value=100)),
        MagicMock(get_name=MagicMock(return_value="sour cream"), get_type=MagicMock(return_value=INGREDIENT_TYPE_SAUCE), get_price=MagicMock(return_value=200)),
        MagicMock(get_name=MagicMock(return_value="chili sauce"), get_type=MagicMock(return_value=INGREDIENT_TYPE_SAUCE), get_price=MagicMock(return_value=300)),
        MagicMock(get_name=MagicMock(return_value="cutlet"), get_type=MagicMock(return_value=INGREDIENT_TYPE_FILLING), get_price=MagicMock(return_value=100)),
        MagicMock(get_name=MagicMock(return_value="dinosaur"), get_type=MagicMock(return_value=INGREDIENT_TYPE_FILLING), get_price=MagicMock(return_value=200)),
        MagicMock(get_name=MagicMock(return_value="sausage"), get_type=MagicMock(return_value=INGREDIENT_TYPE_FILLING), get_price=MagicMock(return_value=300))
    ]


# Фикстура для мокированной базы данных
@pytest.fixture
def mock_database(mock_buns, mock_ingredients):
    """Фикстура для мокирования базы данных с использованием других фикстур для булочек и ингредиентов."""
    mock_db = MagicMock(spec=Database)

    # Подключаем мокированные булочки и ингредиенты
    mock_db.available_buns.return_value = mock_buns
    mock_db.available_ingredients.return_value = mock_ingredients

    return mock_db


@pytest.fixture
def mock_ingredient():
    """
    Фикстура для создания мока ингредиента с параметрами.
    Возвращает мокированный объект класса Ingredient.

    Пример использования:
        ingredient = mock_ingredient("Hot Sauce", 50, INGREDIENT_TYPE_SAUCE)
    """

    def _mock_ingredient(name, price, ingredient_type):
        # Создаем мок для ингредиента с заданными значениями
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        mock_ingredient.get_type.return_value = ingredient_type
        return mock_ingredient

    return _mock_ingredient
