# MealPlanner
A website and interface for J, J, J, J, and B's house meal planning.

## Ticketing System
- Tickets are opened by the users for the following reasons:

| Ticket Type        | Description                                                                                                                                                                            |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Meal Request       | A new recipe option they want included                                                                                                                                                 |
| Ingredient Request | A specific item/ingredient they want added to the shopping list                                                                                                                        |
| Vote               | The user will order a list of *12-15* options for meals the following meal period.<br/>Based on this data the shopping list and meal list is generated for the admin.                  |
| Days Off           | This lets the admin know when users don't need a meal. This lets the admin plan for making less/more of a certain meal and updates the shopping list.                                  |
| Time Change        | This is a request for time change of a specific scheduled meal. This is intended to be used 1-3 days before the meal so that a user can let the cook know they will be late to a meal. |


# recipe_manager.py
- This script allows for the creation and viewing of .yaml recipe files.
- Recipes have the following fields:

| Field       | Data Type        | Notes                                                                                            |
|-------------|------------------|--------------------------------------------------------------------------------------------------|
| Name        | String           | The name of the recipe                                                                           |
| Source      | String           | Where the recipe came from.<br/>This is typically a link to the recipe                           |
| Servings    | Number           | The amount of plates this will make.<br/>It could also be the number of people the recipe serves |
| Tags        | Array of Strings | Short (1-2 word) phrases to quickly find the recipe and sort them later                          |
| Notes       | Array of Strings | Longer notes about the recipe, ingredients, etc.                                                 |
| Ingredients | Array of Strings | Each ingredient is represented as a string in the form  '[count,unit,ingredient name]'           |
| Steps       | Array of Strings | Numbered list of steps to complete the recipe.                                                   |

- Currently the recipe inputs are _not_ validated, and editing is not currently planned to be implemented.
  - It is useful to note, however, that the outputted .yaml files are stored locally in recipe_sources
