def check_ingredient_match(recipes, ingredients):
    missing_ingredients = []

    for rec, ing in zip(recipes, ingredients):
        if rec != ing:
            missing_ingredients.append(rec)

    matches = 100 - ((len(missing_ingredients) / len(recipes)) * 100)

    return matches, missing_ingredients
