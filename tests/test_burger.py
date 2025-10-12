from praktikum import ingredient
from praktikum.burger import Burger
from unittest.mock import Mock 
from praktikum.ingredient_types import *
from data import TestData

class TestBurger:

    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_sauce):
        mock_ingredient = mock_sauce
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, mock_sauce):
        mock_ingredient = mock_sauce
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient(self, mock_sauce, mock_filling):
        mock_ingredient1 = mock_sauce
        mock_ingredient2 = mock_filling

        burger = Burger()
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient2
        assert burger.ingredients[1] == mock_ingredient1

    
    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient1 = Mock()
        mock_ingredient1.get_price.return_value = 100

        mock_ingredient2 = Mock()
        mock_ingredient2.get_price.return_value = 100

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)

        price = burger.get_price()
        assert price == 400

    def test_get_receipt(self, mock_bun, mock_sauce, mock_filling):
        
        mock_ingredient1 = mock_sauce
        mock_ingredient2 = mock_filling

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient1)
        burger.add_ingredient(mock_ingredient2)
        receipt = burger.get_receipt()
        assert receipt == f'(==== {TestData.name_bun} ====)\n= {str(mock_ingredient1.get_type()).lower()} {TestData.name_sauce} =\n= {str(mock_ingredient2.get_type()).lower()} {TestData.name_filling} =\n(==== {TestData.name_bun} ====)\n\nPrice: {TestData.burger_price}'
        

