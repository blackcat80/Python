import datetime
from recipe import Recipe
from colorama import Fore, Back, Style

fecha_actual = datetime.datetime.now()

class Book:
    def __init__(self, name):                                                # método __init__ inicializa los atributos de la clase
        self.name = name                                                     # nombre del libro
        self.last_update = fecha_actual                                      # la fecha de la última actualización  
        self.creation_date = fecha_actual                                    # la fecha de creación
        self.recipes_list = {"starter": [], "lunch":[], "dessert":[]}        # un diccionario con 3 claves "starter", "lunch", "dessert"

    def get_recipe_by_name(self, name):
        for recipe_type, recipes in self.recipes_list.items():
            for recipe in recipes:
                if recipe.name == name:
                    #print(recipe)
                    return recipe
        print(Fore.RED + "Recipe not found." + Fore.RESET)
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            return self.recipes_list[recipe_type]
        else:
            print(Fore.RED + "Invalid recipe type." + Fore.RESET)
            return None
            
    def add_recipe(self, recipe):    
        if not isinstance(recipe, Recipe):
            raise TypeError(Fore.RED + "Only recipe objects can be added to the book." + Fore.RESET)
        recipe_type = recipe.recipe_type
        if recipe_type in self.recipes_list:
            self.recipes_list[recipe_type].append(recipe)
            self.last_update = fecha_actual
        else:
            print("Invalid recipe type.")

