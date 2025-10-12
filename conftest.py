import pytest
from praktikum.burger import Burger
from unittest.mock import Mock 
from praktikum.ingredient_types import *
from data import TestData



@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = TestData.name_bun
    mock_bun.get_price.return_value = TestData.mock_bun_price
    return mock_bun

@pytest.fixture()
def mock_sauce():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_ingredient.get_name.return_value = TestData.name_sauce
    mock_ingredient.get_price.return_value = TestData.mock_sauce_price
    return mock_ingredient

@pytest.fixture()
def mock_filling():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_ingredient.get_name.return_value = TestData.name_filling
    mock_ingredient.get_price.return_value = TestData.mock_filling_price
    return mock_ingredient