# MealPlanner
A website and interface for J, J, J, J, and B's house meal planning.

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
