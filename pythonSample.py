"""
Recipe Book - Version Controlled Project

To demonstrate version control with Git, I created a recipe book project that includes:
1. Initializing a Git repository
2. Adding recipe files and committing with messages
3. Creating and merging branches
4. Simulating and resolving a merge conflict
"""

# Initial Recipe - Added in the main branch and committed
recipes = {
    "Pancakes": {
        "ingredients": ["2 cups flour", "2 eggs", "1.5 cups milk", "1 tbsp sugar", "1 tsp salt", "1 tbsp baking powder"],
        "instructions": "Mix ingredients. Pour batter on a hot griddle. Flip when bubbles form. Serve warm."
    },
    "Grilled Cheese": {
        "ingredients": ["2 slices bread", "2 slices cheese", "1 tbsp butter"],
        "instructions": "Butter the bread. Place cheese between slices. Grill until golden brown on both sides."
    }
}

# Simulated Merge Conflict:
recipes["Pancakes"]["ingredients"] = [
    "2 cups flour", "2 eggs", "1.5 cups milk", "1 tbsp sugar", 
    "1 tsp salt", "1 tbsp baking powder", "1 tsp vanilla"
]



