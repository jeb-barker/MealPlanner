# This program allows the user to see/modify/add recipies in YAML format

import yaml
STATE_ENUM = {"START": 1, "RECIPE_LIST": 2, "ADD_RECIPE": 3, "ADD_INGREDIENT": 4, "NAME": 5, "SOURCE" : 6, "SERVINGS": 7, "TAGS": 8, "NOTES": 9, "ADD_STEP": 10}
STATE = STATE_ENUM["START"]


def print_recipe_list():
    pass


def print_options():
    global STATE_ENUM
    global STATE
    if STATE == STATE_ENUM["START"]:
        print("1. View List of Recipies:")
        print("2. Add Recipe")
    if STATE == STATE_ENUM["RECIPE_LIST"]:
        print_recipe_list()
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
        print("Enter a new step or \"-1\" to stop adding ingredients")


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
        if int(user_input) == 2:
            STATE = STATE_ENUM["ADD_RECIPE"]
            print_options()

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
            servings = user_input



if __name__ == "__main__":
    main()