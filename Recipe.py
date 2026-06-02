from Ingredient import Ingredient

class Recipe:
    def __init__(self, title: str, ingredients: list):
        self.title = title
        self.ingredients = []
        for ingredient in ingredients:
            self.add_ingredient(ingredient)

    def add_ingredient(self, ingredient: Ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)
        else:
            index = self.ingredients.index(ingredient)
            self.ingredients[index].quantity += ingredient.quantity

    @staticmethod
    def is_valid_ratio(ratio) -> bool:
        try:
            return ratio > 0
        except:
            return False

    def scale(self, ratio: float):
        if not Recipe.is_valid_ratio(ratio):
            return None
        res = Recipe(self.title, [])
        for ingredient in self.ingredients:
            res.add_ingredient(Ingredient(ingredient.name, ingredient.quantity * ratio, ingredient.unit))
        return res


    def __len__(self):
        return len(self.ingredients)

    def __str__(self):
        res = f"{self.title}:\n"
        for ingredient in self.ingredients:
            res += "- " + str(ingredient) + "\n"
        return res

pizza = Recipe("Pizza",
               [Ingredient("pour", 100.0, "g"),
                Ingredient("pour", 200.0, "g"),
                Ingredient("pour", 300.0, "kg"),
                Ingredient("milk", 400.0, "ml"),
                Ingredient("cheese", 5.0, "kg"),])
