import pytest
from unittest.mock import Mock 
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def burger():
    return Burger()

@pytest.fixture(params=[
                        ('Флюорисцентная булка R2-D3', 988),
                        ('Краторная булка N-200i', 1255),])
def mock_bun(request):
    bun = Mock()
    bun.get_name.return_value= request.param[0]
    bun.get_price.return_value = request.param[1]
    return bun

@pytest.fixture(params=[
                        ('Хрустящие минеральные кольца', 300),
                        ('Сыр с астероидной плесенью', 4142),])
def mock_ingredient(request):
    ingredient = Mock()
    ingredient.get_name.return_value= request.param[0]
    ingredient.get_price.return_value = request.param[1]
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient

@pytest.fixture(params=[
                        ('Spicy-X',90),
                        ('Соус фирменный Space Sauce',80 ),])
def mock_ingredient_1(request):
    ingredient_1 = Mock()
    ingredient_1.get_name.return_value= request.param[0]
    ingredient_1.get_price.return_value = request.param[1]
    ingredient_1.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient_1

