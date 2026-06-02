from Ingredient import Ingredient
from Recipe import Recipe


class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipe = recipe.scale(portions)
        for ingredient in recipe.ingredients:
            self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title: str):
        for i in range(len(self._items), -1, -1):
            if self._items[i][1] == title:
                self._items.pop(i)

    def get_list(self) -> list:
        res_ingredients = dict()
        for ingredient, title in self._items:
            res_ingredients[(ingredient.name, ingredient.unit)] = res_ingredients.get((ingredient.name, ingredient.unit), 0) + ingredient.quantity
        res_list = []
        for name, unit, quantity in res_ingredients.items():
            res_list.append(Ingredient(name, quantity, unit))
        res_list.sort(key=lambda ingredient: ingredient.name)
        return res_list

    def __add__(self, other):
        new_shoppinglist = ShoppingList()
        for pair in self._items:
            new_shoppinglist._items.append(pair)
        for pair in other._items:
            new_shoppinglist._items.append(pair)
        return new_shoppinglist
