from pprint import pprint
cook_book = {}
ingredient = {}
with open("recipes.txt", 'r', encoding='utf-8') as file:
    for line in file:
        ingredients = []
        dish = line.strip()
        ingredients_quantity = int(file.readline().strip())
        for i in range(ingredients_quantity):
            string_ingredient = file.readline().strip().split('|')
            ingredient = {'ingredient_name': string_ingredient[0], 'quantity': string_ingredient[1], 'measure': string_ingredient[2]}
            ingredients.append(ingredient)
        file.readline()
        cook_book[dish] = ingredients
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    dict_ingredients = {}
    for dish in dishes:
        for i in range(len(cook_book[dish])):
            if cook_book[dish][i]['ingredient_name'] not in dict_ingredients:
                dict_ingredients[cook_book[dish][i]['ingredient_name']] = {'measure':cook_book[dish][i]['measure'], 'quantity':int(cook_book[dish][i]['quantity'])*person_count}
            else:
                count_ingredients = int(dict_ingredients[cook_book[dish][i]['ingredient_name']]['quantity']) + int(cook_book[dish][i]['quantity']) * person_count
                dict_ingredients[cook_book[dish][i]['ingredient_name']] = {'measure':cook_book[dish][i]['measure'], 'quantity':count_ingredients}
    pprint(dict_ingredients)

get_shop_list_by_dishes(['Омлет', 'Фахитос'],2)




