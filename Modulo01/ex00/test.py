from book import Book
from recipe import Recipe

book = Book("Libro de Cocina")
recipe = Recipe("Tarta de Manzana", 5, 10, ["manzanas", "hojaldre", "crema"], "Receta de Tarta de Manzana", "dessert") 
book.add_recipe(recipe)

#print("Test 1: Bien!\nTest 2: ", end ="")
#print(book.get_recipe_by_name("The Beatles"))
print(book.get_recipe_by_name("Tarta de Manzana"))
print(book.get_recipe_by_name("Tarta"))
