import streamlit as st
import openai

#replace YOUR-OPENAI-API-KEY with your openAI API key
openai.api_key = "YOUR-OPENAI-API-KEY"

st.header('Grocery List Creator')
st.subheader("Create your Grocery list by selecting your meals below and the click 'Create Grocery List.' You can also ask our resident Chef to suggest some recipes for you after you have created your grocery list.")

#Create categories of meals and the meals in each of those categories
categories = ['Dinner', 'Lunch', 'Breakfast']
dinner_meals = ['Bolognese', 'Chicken and rice', 'Smash Burgers', 'Pork Ginger Soup', 'Greek Salad', 'Stir fry', 'Taco night', 'Sausage kale pasta bake', 'Carnitas', 'Salmon cakes', 'Turkey feta meatballs', 'Chicken chili', 'Beef chili', 'Corn chowder', 'Flank steak sandwiches']
breakfast_meals = ['Yogurt bowls', 'Bagels', 'All American breakfast', 'Smoothies', 'Breakfast sandwiches']
lunch_meals = ['Turkey sandwich', 'Mac and cheese']

# Create a dictionary to store the ingredients for each meal
meal_ingredients = {
    'Bolognese': ['Ground beef', 'ground pork', 'Onion', 'carrot', 'celery', 'chicken broth', 'Tomato paste'],
    'Chicken and rice': ['Chicken breasts', 'Rice', 'Broccoli', 'Cheddar Cheese'],
    'Smash Burgers': ['Ground beef', 'Buns', 'Cheese', 'Lettuce', 'Tomato', 'pickle'],
    'Pork Ginger Soup': ['ground pork', 'ginger', 'miso broth', 'spinach or kale', 'scallions', 'garlic'],
    'Greek Salad': ['Olives', 'feta', 'cucumber', 'red onion', 'cherry tomatoes'],
    # Assign the remaining meals and their ingredients here
}

selected_categories = st.multiselect('Select categories', categories)

selected_meals = []
selected_ingredients = []
for category in selected_categories:
    if category == 'Dinner':
        selected_meals += st.multiselect('Select dinner meals', dinner_meals)
    elif category == 'Lunch':
        selected_meals += st.multiselect('Select lunch meals', lunch_meals)
    elif category == 'Breakfast':
        selected_meals += st.multiselect('Select breakfast meals', breakfast_meals)

selected_ingredients = [meal_ingredients[meal] for meal in selected_meals if meal in meal_ingredients]

# Generate consolidated grocery list
grocery_list = {}
if selected_ingredients:
    for ingredients in selected_ingredients:
        for item in ingredients:
            grocery_list[item] = grocery_list.get(item, 0) + 1

if st.button('Create Grocery List'):
    if selected_ingredients:
        st.write("Consolidated Grocery List:")
        for item, count in grocery_list.items():
            st.write(f"{count} {item}")
    else:
        st.write("No ingredients found for the selected meals.")

# This button will let the user have OpenAI suggest recipes based on their grocery list
if st.button('Suggest me more recipes'):
    if grocery_list:
        prompt = "Assume that I have some basic spices at my disposal. You are an expert Chef who responds in neat paragraphs, with bullet points where needed. You will be given a list of grocery items and I would like you to provide 3 recipes based on the list of grocery items"
        prompt += ", Here is the list of grocery items that i have: ".join(grocery_list.keys())

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=250,
            n=3,  # Number of recipe suggestions to generate
            stop=None,
            temperature=0.9,
        )

        st.write("Recipe Suggestions:")
        for suggestion in response.choices:
            st.write(suggestion.text.strip())
    else:
        st.write("No grocery list available. Please create a grocery list first.")
