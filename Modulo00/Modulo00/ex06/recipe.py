
cookbook = {
    "bocadillo": {
        "ingredients": ["jamón", "pan", "queso", "tomate"],
        "meal": "almuerzo",
        "prep_time": 10
    },
    "tarta": {
        "ingredients": ["harina", "azúcar", "huevos"],
        "meal": "postre",
        "prep_time": 60
    },
    "ensalada": {
        "ingredients": ["aguacate", "rúcula", "tomates", "espinacas"],
        "meal": "almuerzo",
        "prep_time": 15
    }
}

def print_recipe_names():
    for recipe_name in cookbook:
        print(recipe_name)

        
def print_recipe_details(name):
    recipe = cookbook.get(name)
    if recipe is None:
        print(f"La receta '{name}' no existe en el cookbook.")
        return
    print(f"Nombre: {name}")
    print(f"Ingredientes: {', '.join(recipe['ingredients'])}")
    print(f"Tipo de comida: {recipe['meal']}")
    print(f"Tiempo de preparación: {recipe['prep_time']} minutos")


def delete_recipe(name):
    if cookbook.pop(name, None) is None:
        print(f"La receta '{name}' no existe en el cookbook.")
    else:
        print(f"La receta '{name}' ha sido eliminada del cookbook.")


def add_recipe():
    name = input("Ingresa el nombre de la receta: ")
    
    print("Ingresa la lista de ingredientes:")
    ingredients = list(iter(input, ''))
       
    meal = input("Ingresa el tipo de comida: ")
    prep_time = int(input("Ingresa el tiempo de preparación en minutos: "))
    cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    print(f"La receta '{name}' ha sido agregada al cookbook.")

def main():
    while True:
        print("\nWelcome to the Python Cookbook !")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        try:
            choice = int(input("Ingresa el número de la opción: "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if choice == 1:
            add_recipe()            
        elif choice == 2:
            name = input("Ingresa el nombre de la receta que deseas eliminar: ")
            delete_recipe(name)            
        elif choice == 3:
            name = input("Ingresa el nombre de la receta: ")
            print_recipe_details(name)        
        elif choice == 4:
            print_recipe_names()
        elif choice == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Ingresa una opción válida (1-5)")


# Ejecutar el programa principal
if __name__ == '__main__':
    main()
