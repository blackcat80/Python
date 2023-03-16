import unittest
from book import Book
from recipe import Recipe
from colorama import Fore, Style

class TestBook(unittest.TestCase):
    
    def setUp(self):
        self.book = Book("Libro de Cocina")
        self.recipe1 = Recipe("Tarta de Manzana", 5, 10, ["manzanas", "hojaldre", "crema"], "Receta de Tarta de Manzana", "dessert") 
        self.recipe2 = Recipe("Pollo al Curry", 3, 30, ["pollo", "cebolla", "ajo", "curry", "crema"], "Receta de Pollo al Curry", "lunch") 
        self.recipe3 = Recipe("Ensalada César", 2, 15, ["lechuga", "pollo", "pan", "queso", "salsa César"], "Receta de Ensalada César", "starter") 
        self.book.add_recipe(self.recipe1)
        self.book.add_recipe(self.recipe2)
        self.book.add_recipe(self.recipe3)
        
    def test_get_recipe_by_name(self):
        # Test 1: obtener receta existente por nombre
        recipe = self.book.get_recipe_by_name("Tarta de Manzana")
        self.assertIsNotNone(recipe, f"{Fore.RED}Error en Test 1: no se encontró la receta Tarta de Manzana{Style.RESET_ALL}")
        self.assertEqual(recipe.name, "Tarta de Manzana", f"{Fore.RED}Error en Test 1: se encontró la receta {recipe.name} en lugar de Tarta de Manzana{Style.RESET_ALL}")
        
        # Test 2: obtener receta inexistente por nombre
        recipe = self.book.get_recipe_by_name("Tarta")
        self.assertIsNone(recipe, f"{Fore.RED}Error en Test 2: se encontró una receta inexistente{Style.RESET_ALL}")

    def test_get_all_recipes(self):
        # Test 3: obtener todos los recetas
        recipes = self.book.get_all_recipes()
        self.assertIsNotNone(recipes, f"{Fore.RED}Error en Test 3: no se encontró ninguna receta{Style.RESET_ALL}")
        self.assertEqual(len(recipes), 3, f"{Fore.RED}Error en Test 3: se encontró {len(recipes)} recetas{Style.RESET_ALL}")
        
        # Test 4: obtener todos los recetas con nombre igual a "Tarta de Manzana"
        recipes = self.book.get_all_recipes("Tarta de Manzana")
        self.assertIsNotNone(recipes, f"{Fore.RED}Error en Test 4: no se encontró ninguna receta con nombre igual a Tarta de Manzana{Style.RESET_ALL}")
        self.assertEqual(len(recipes), 1, f"{Fore.RED}Error en Test 4: se encontró {len(recipes)} recetas con nombre igual a Tarta de Manzana{Style.RESET_ALL}")

        # Test 5: obtener todos los recetas con nombre igual a "Tarta"
        recipes = self.book.get_all_recipes("Tarta")
        self.assertIsNotNone(recipes, f"{Fore.RED}Error en Test 5: no se encontró ninguna receta con nombre igual a Tarta{Style.RESET_ALL}")
        self.assertEqual(len(recipes), 2, f"{Fore.RED}Error en Test 5: se encontró {len(recipes)} recetas con nombre igual a Tarta{Style.RESET_ALL}")
    
    def test_get_recipe_by_types(self):
        # Test 6: obtener receta existente por tipo
        recipe = self.book.get_recipe_by_types(["manzanas", "hojaldre", "crema"])
        self.assertIsNotNone(recipe, f"{Fore.RED}Error en Test 6: no se encontró la receta Tarta de Manzana{Style.RESET_ALL}")
        self.assertEqual(recipe.name, "Tarta de Manzana", f"{Fore.RED}Error en Test 6: se encontró la receta {recipe.name} en lugar de Tarta de Manzana{Style.RESET_ALL}")
        
        # Test 7: obtener receta inexistente por tipo
        recipe = self.book.get_recipe_by_types(["pollo", "cebolla", "ajo", "curry", "crema"])
        self.assertIsNone(recipe, f"{Fore.RED}Error en Test 7: se encontró una receta inexistente{Style.RESET_ALL}")

    def test_add_recipe(self):
        # Test 8: agregar receta
        recipe = self.book.add_recipe(self.recipe1)
        self.assertIsNotNone(recipe, f"{Fore.RED}Error en Test 8: no se agregó la receta Tarta de Manzana{Style.RESET_ALL}")
        self.assertEqual(recipe.name, "Tarta de Manzana", f"{Fore.RED}Error en Test 8: se agregó la receta {recipe.name} en lugar de Tarta de Manzana{Style.RESET_ALL}")
        
        # Test 9: agregar receta con nombre igual a "Tarta de Manzana"
        recipe = self.book.add_recipe(self.recipe1)
        self.assertIsNotNone(recipe, f"{Fore.RED}Error en Test 9: no se agregó la receta Tarta de Manzana{Style.RESET_ALL}")
        self.assertEqual(recipe.name, "Tarta de Manzana", f"{Fore.RED}Error en Test 9: se agregó la receta {recipe.name} en lugar de Tarta de Manzana{Style.RESET_ALL}")
                
if __name__ == '__main__':
    unittest.main()