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

solved_ingredients = set()
while True:
    for allergen,ingredients in all_allergens.items():
        if len(ingredients) == 1:
            solved_ingredients.update(ingredients)
            all_allergens[allergen] = [ingredients.pop()]
        else:
            all_allergens[allergen] = [ingredient for ingredient in ingredients if ingredient not in solved_ingredients]
            
    if solved_ingredients == all_allergenic_ingredients:
        break

ingredients_list = ",".join([value[0] for key,value in sorted(all_allergens.items())])
print(ingredients_list)