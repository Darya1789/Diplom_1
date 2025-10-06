import pytest
from praktikum.burger import Burger
from unittest.mock import Mock 
from praktikum.ingredient_types import *



@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Булочка"
    mock_bun.get_price.return_value = 100
    return mock_bun