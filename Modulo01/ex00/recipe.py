from colorama import Fore, Style

class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

        # Comprobando las condiciones:
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl not in range(1, 6):
            raise ValueError(Fore.RED + "ERROR: Nivel de dificultad no válido, escoja un nivel del 1 al 5" + Fore.RESET)            
        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            raise ValueError(Fore.RED + "ERROR: Formato de tiempo no válido" + Fore.RESET)
        if self.recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError(Fore.RED + "ERROR: Tipo de receta no valida" + Fore.RESET)

    def __str__(self) -> str:        
        txt = "\nReceta: {}\nNivel de cocina: {}\nTiempo de cocción: {} minutos\nIngredientes: {}\nDescripción: {}\nTipo de receta: {}\n".format(
            self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt
