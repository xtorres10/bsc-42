cookbook = {
    'Sandwich': {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'], 'meal': 'lunch', 'prep_time': 10},
    'Cake': {'ingredients': ['flour', 'sugar', 'eggs'], 'meal': 'dessert', 'prep_time': 60},
    'Salad': {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal': 'lunch', 'prep_time': 15}
    }   

def print_recipes():
    for c in cookbook:
        print(c)

def print_details():
    name = input('Nombre de la receta:\n')


def delete_recipe():
    name = input('Nombre de la receta:\n').title()
    try:
        del cookbook[name]
    except KeyError:
        print('No hay recetas')



def add_recipe():
    name = input('Enter a name:')
    ingredients = []
    i = input('Enter ingredients:')
    while i != '':
        i = input()
        if i != '':
            ingredients.append(i)
    tmeal = input('Enter a meal type:')
    time = input('Enter a preparation time:')
    # dict(name = {'ingredients': dict(ingredients), 'meal': meal, 'prep_time': time})


def main():
    print('Welcome to the Python Cookbook !') 
    while True:
        print('List of available option:\
                \n1: Add a recipe\
                \n2: Delete a recipe\
                \n3: Print a recipe\
                \n4: Print the cookbook\
                \n5: Quit')
        opt = input('Please select an option:\n')
        if opt == '1':
            add_recipe()
        elif opt == '2':
            delete_recipe()
        elif opt == '3':
            print_details()
        elif opt == '4':
            print_recipes()
        elif opt == '5':
            print('\nCookbook closed. Goodbye !')
            break
        else:
            print('Sorry, this option does not exist.')
        print()

if __name__ == '__main__':
    main()