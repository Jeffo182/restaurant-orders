import pandas as pd
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load(source_path)

    def load(self, path):
        #criando dataframe
        data_csv = pd.read_csv(path)
        dishes = {}

        for index, row in data_csv.iterrows():
            dish_name = row["dish"]
            dish_price = float(row["price"])
            ingredient_name = row["ingredient"]
            recipe_amount = int(row["recipe_amount"])
            #verificando se prato ja existe
            if dish_name in dishes:
                dish = dishes[dish_name]
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)
            else:
                dish = Dish(dish_name, dish_price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)
                dishes[dish_name] = dish

        self.dishes = set(dishes.values())
