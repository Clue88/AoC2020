from collections import OrderedDict

def main():
    f = open('21-input.txt', 'r')
    lines = f.read().split('\n')[:-1]
    f.close()

    foods = []
    allergens = []
    for line in lines:
        foods.append((line.split(' (')[0].split(' '), line.split('contains ')[1][:-1].split(', ')))
        allergens.extend(line.split('contains ')[1][:-1].split(', '))
    
    allergens = remove_duplicates(allergens)

    possibles = {}
    for allergen in allergens:
        allergen_foods = []
        ingredients = []
        for food in foods:
            if allergen in food[1]:
                allergen_foods.append(food[0])
                ingredients.extend(food[0])
        ingredients = remove_duplicates(ingredients)
        
        matching = []
        for ingredient in ingredients:
            failed = False
            for allergen_food in allergen_foods:
                if ingredient not in allergen_food:
                    failed = True
                    break
            if not failed:
                matching.append(ingredient)
        
        possibles[allergen] = matching

    finals = {}
    while len(finals) < len(possibles):
        for allergen, ingredients in possibles.items():
            if len(ingredients) == 1:
                finals[allergen] = ingredients[0]
                for key in possibles.keys():
                    if key == allergen:
                        continue
                    if ingredients[0] in possibles[key]:
                        possibles[key].remove(ingredients[0])

    bad = []
    ordered_finals = OrderedDict(sorted(finals.items()))
    for key, value in ordered_finals.items():
        bad.append(value)
    result = ','.join(bad)

    print('Result:', result)

def remove_duplicates(_list):
    temp = []
    for i in _list:
        if i not in temp:
            temp.append(i)
    return temp

if __name__ == '__main__':
    main()

# Result: 
