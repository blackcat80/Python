from colorama import Fore, Back, Style

class Recipe():
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name                        # valor string
        self.cooking_lvl = cooking_lvl          # valor int
        self.cooking_time = cooking_time        # valor int
        self.ingredients = ingredients          # valor lista, con comillas separadas por comas y entre corchetes
        self.description = description          # valor string con comillas 
        self.recipe_type = recipe_type          # valor string con comillas

        # comprobando las condiciones:
        if self.cooking_lvl not in range(1, 6) or not isinstance(self.cooking_lvl, int):
            print(Fore.RED + "ERROR: Nivel de dificultad no válido, escoja un nivel del 1 al 5" + Fore.RESET)            
            exit()
        if self.cooking_time < 0 or not isinstance(self.cooking_time, int):
            print(Fore.RED + "ERROR: Formato de tiempo no válido" + Fore.RESET)
            exit()
        if self.recipe_type not in ["starter", "lunch", "dessert"]:
            print(Fore.RED + "ERROR: Tipo de receta no valida" + Fore.RESET)
            exit()

    def __str__(self):        
        txt = "\nReceta: {}\nNivel de cocina: {}\nTiempo de cocción: {} minutos\nIngredientes: {}\nDescripción: {}\nTipo de receta: {}\n".format(
            self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type)
        return txt
    


