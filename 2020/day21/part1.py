with open("day21/input.txt", "r") as f:
    raw_recipes = [line.strip("\n") for line in f]

recipes = []
all_allergens = dict()
all_allergenic_ingredients = set()
non_allergenic_ingredient_count = 0

for recipe in raw_recipes:
    ingredients, allergens = recipe.split("(contains")
    allergens = allergens.strip(" )").split(", ")
    ingredients = ingredients.strip(" ").split(" ")

    recipes.append({"ingredients":ingredients, "allergens":allergens})

    for allergen in allergens:
        if allergen not in all_allergens:
            all_allergens[allergen] = set(ingredients)
        else:
            all_allergens[allergen].intersection_update(ingredients)

all_allergenic_ingredients.update(*all_allergens.values())

for recipe in recipes:
    non_allergenic_ingredients = [ingredient for ingredient in recipe["ingredients"] if ingredient not in all_allergenic_ingredients]
    non_allergenic_ingredient_count += len(non_allergenic_ingredients)

print(non_allergenic_ingredient_count)