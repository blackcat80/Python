import datetime
from recipe import Recipe
from colorama import Fore, Style

class Book:
    def __init__(self, name):                                               # método __init__ inicializa los atributos de la clase
        self.name = name                                                    # nombre del libro
        self.last_update = datetime.datetime.now()                          # la fecha de la última actualización 
        self.creation_date = self.last_update                               # la fecha de creación
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}     # un diccionario con 3 claves "starter", "lunch", "dessert"

    def get_recipe_by_name(self, name):
        for recipe_type, recipes in self.recipes_list.items():
            for recipe in recipes:
                if recipe.name == name:
                    return recipe
        print(Fore.RED + f"Recipe '{name}' not found." + Style.RESET_ALL)
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            return self.recipes_list[recipe_type]
        else:
            print(Fore.RED + f"Invalid recipe type '{recipe_type}'." + Style.RESET_ALL)
            return None
            
    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise TypeError(Fore.RED + "Only recipe objects can be added to the book." + Style.RESET_ALL)
        recipe_type = recipe.recipe_type
        if recipe_type in self.recipes_list:
            self.recipes_list[recipe_type].append(recipe)
            self.last_update = datetime.datetime.now()
        else:
            print(Fore.RED + f"Invalid recipe type '{recipe_type}'." + Style.RESET_ALL)

