from Recipe import Recipe


class DietaryRecipe (Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=[]):
        super().__init__(title, ingredients)
        self._diet_type = diet_type

    def scale(self, ratio: float):
        scaled = super().scale(ratio)
        if scaled is None:
            return None
        return DietaryRecipe(self.title, self._diet_type, scaled.ingredients)

    def __str__(self):
        return f"[{self._diet_type}] " + super().__str__()