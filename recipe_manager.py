# This program allows the user to see/modify/add recipies in YAML format

import oyaml as yaml
import os
import io

# global enum and state
STATE_ENUM = {"START": 1, "RECIPE_LIST": 2, "ADD_RECIPE": 3, "ADD_INGREDIENT": 4, "NAME": 5, "SOURCE" : 6, "SERVINGS": 7, "TAGS": 8, "NOTES": 9, "ADD_STEP": 10, "CHOOSE_RECIPE": 11}
STATE = STATE_ENUM["START"]


def print_recipe_list():
    directory = os.fsencode("./recipe_sources")

    recipes = []
    recipe_number = 1
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        filename = "./recipe_sources/" + filename
        if filename.endswith(".yaml"):
            with open(filename) as stream:
                try:
                    curr_recipe = yaml.safe_load(stream)
                    recipes.append(curr_recipe)
                    print(str(recipe_number) + ".\t" + curr_recipe["name"])
                except yaml.YAMLError as exc:
                    print(exc)
    return recipes


def print_options():
    global STATE_ENUM
    global STATE
    if STATE == STATE_ENUM["START"]:
        print("1. View List of Recipies:")
        print("2. Add Recipe")
    if STATE == STATE_ENUM["RECIPE_LIST"]:
        print("Select one of the recipies below:")
    if STATE == STATE_ENUM["ADD_RECIPE"]:
        print("You would like to add a recipe.\nPlease enter the following fields (don't leave them blank or I'll cry).")
    if STATE == STATE_ENUM["NAME"]:
        print("Enter the name of the recipe:")
    if STATE == STATE_ENUM["SOURCE"]:
        print("Enter where you got it from (link is preferred):")
    if STATE == STATE_ENUM["SERVINGS"]:
        print("Enter how many servings it makes:")
    if STATE == STATE_ENUM["TAGS"]:
        print("Enter a new tag or \"-1\" to stop adding tags:")
    if STATE == STATE_ENUM["NOTES"]:
        print("Enter a new note or \"-1\" to stop adding notes")
    if STATE == STATE_ENUM["ADD_INGREDIENT"]:
        print("Enter the count, unit, and name of the ingredient:\n(e.g. \"2,clove,garlic\")\n")
    if STATE == STATE_ENUM["ADD_STEP"]:
        print("Enter a new step or \"-1\" to stop adding steps")
    if STATE == STATE_ENUM["CHOOSE_RECIPE"]:
        print("Choose a recipe from above (or -1 to go back):")


def get_recipe_from_user():
    global STATE
    global STATE_ENUM
    STATE = STATE_ENUM["NAME"]
    print_options()
    # get recipe name
    user_input = input("")
    name = user_input

    STATE = STATE_ENUM["SOURCE"]
    print_options()
    # get recipe source
    user_input = input("")
    source = user_input

    STATE = STATE_ENUM["SERVINGS"]
    print_options()
    # get recipe servings
    user_input = input("")
    servings = int(user_input)

    STATE = STATE_ENUM["TAGS"]
    print_options()
    tags = []
    # get recipe servings
    user_input = input("")
    while user_input != "-1":
        tags.append(user_input)
        print_options()
        user_input = input("")

    STATE = STATE_ENUM["NOTES"]
    print_options()
    notes = []
    # get recipe servings
    user_input = input("")
    while user_input != "-1":
        notes.append(user_input)
        print_options()
        user_input = input("")

    STATE = STATE_ENUM["ADD_INGREDIENT"]
    print_options()
    ingredients = []
    # get recipe servings
    user_input = input("")
    while user_input != "-1":
        split_input = user_input.split(",")
        ingredients.append("["+split_input[0]+","+split_input[1]+","+split_input[2]+"]")
        print_options()
        user_input = input("")

    STATE = STATE_ENUM["ADD_STEP"]
    print_options()
    steps = []
    # get recipe servings
    user_input = input("")
    while user_input != "-1":
        steps.append(user_input)
        print_options()
        user_input = input("")

    output_yaml(name, source, servings, tags, notes, ingredients, steps)


def output_yaml(name, source, servings, tags, notes, ingredients, steps):
    data = {
        'name': name,
        'source': source,
        'servings': servings,
        'tags': tags,
        'notes': notes,
        'ingredients': ingredients,
        'steps': steps
    }

    # Write YAML file
    with io.open('./recipe_sources/'+name.replace(" ", "_")+'.yaml', 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)


def main():
    global STATE_ENUM
    global STATE
    print("\t\tRecipe Manager\n__________________________________\n")

    while True:
        STATE = STATE_ENUM["START"]
        print_options()
        #getting valid options from the user (0 or 1)
        user_input = input("")
        while int(user_input) != 1 and int(user_input) != 2 and int(user_input) != -1:
            print_options()
            user_input = input("")
        if int(user_input) == -1:
            break
        if int(user_input) == 1:
            STATE = STATE_ENUM["RECIPE_LIST"]
            print_options()
            options = print_recipe_list()
            user_input = int(input(""))
            # TODO: validate:
            print(options[user_input-1])

            STATE = STATE_ENUM["CHOOSE_RECIPE"]
            print_options()
        if int(user_input) == 2:
            STATE = STATE_ENUM["ADD_RECIPE"]
            print_options()
            get_recipe_from_user()



if __name__ == "__main__":
    main()