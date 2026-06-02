import pytest

from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList


#Ingredient

def test_ingredient_init():
    ing = Ingredient("Мука", 500.0, "г")
    assert ing.name == "Мука"
    assert ing.quantity == 500.0
    assert ing.unit == "г"


def test_ingredient_str():
    assert str(Ingredient("Мука", 500.0, "г")) == "Мука: 500.0 г"


def test_eq_same_name_unit():
    assert Ingredient("Мука", 500.0, "г") == Ingredient("Мука", 100.0, "г")


def test_eq_diff_name():
    assert Ingredient("Мука", 500.0, "г") != Ingredient("Соль", 500.0, "г")


def test_eq_diff_unit():
    assert Ingredient("Мука", 500.0, "г") != Ingredient("Мука", 500.0, "кг")


#Recipe

def test_recipe_init():
    ing = Ingredient("Мука", 500.0, "г")
    recipe = Recipe("Хлеб", [ing])
    assert recipe.title == "Хлеб"
    assert recipe.ingredients == [ing]


def test_add_new_ingredient():
    recipe = Recipe("Хлеб", [])
    recipe.add_ingredient(Ingredient("Мука", 500.0, "г"))
    assert len(recipe.ingredients) == 1


def test_add_existing_sums():
    recipe = Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")])
    recipe.add_ingredient(Ingredient("Мука", 100.0, "г"))
    assert len(recipe.ingredients) == 1
    assert recipe.ingredients[0].quantity == 600.0


def test_scale_returns_new():
    recipe = Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")])
    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert recipe.ingredients[0].quantity == 500.0


def test_scale_multiplies():
    recipe = Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")])
    scaled = recipe.scale(2)
    assert scaled.ingredients[0].quantity == 1000.0


def test_scale_invalid_ratio():
    recipe = Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")])
    with pytest.raises(ValueError):
        recipe.scale(0)


def test_recipe_len():
    recipe = Recipe("Хлеб", [Ingredient("Мука", 500.0, "г"),
                             Ingredient("Соль", 10.0, "г")])
    assert len(recipe) == 2


#ShoppingList

def test_add_recipe():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")]), 1)
    assert len(sl.get_list()) == 1


def test_add_recipe_invalid_portions():
    sl = ShoppingList()
    with pytest.raises(ValueError):
        sl.add_recipe(Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")]), 0)


def test_remove_recipe():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")]), 1)
    sl.remove_recipe("Хлеб")
    assert sl.get_list() == []


def test_remove_missing_recipe():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")]), 1)
    sl.remove_recipe("Пицца")
    assert len(sl.get_list()) == 1


def test_get_list_sums():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")]), 1)
    sl.add_recipe(Recipe("Пирог", [Ingredient("Мука", 300.0, "г")]), 1)
    result = sl.get_list()
    assert len(result) == 1
    assert result[0].quantity == 800.0


def test_get_list_sorted():
    sl = ShoppingList()
    sl.add_recipe(Recipe("Блюдо", [Ingredient("Соль", 10.0, "г"),
                                   Ingredient("Мука", 500.0, "г")]), 1)
    names = [ing.name for ing in sl.get_list()]
    assert names == sorted(names)


def test_add_lists():
    sl1 = ShoppingList()
    sl1.add_recipe(Recipe("Хлеб", [Ingredient("Мука", 500.0, "г")]), 1)
    sl2 = ShoppingList()
    sl2.add_recipe(Recipe("Пирог", [Ingredient("Соль", 10.0, "г")]), 1)
    combined = sl1 + sl2
    assert len(combined.get_list()) == 2
    assert len(sl1.get_list()) == 1
    assert len(sl2.get_list()) == 1
