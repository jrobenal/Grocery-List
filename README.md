# Grocery-List
Streamlit app that allows users to select their meals and generate a grocery list. Also allows for the user to utilize generative AI to create additional recipes based on the grocery list

This is a Python script that allows users to create a grocery list by selecting meals from different categories. It also provides recipe suggestions based on the selected grocery items using OpenAI's text generation capabilities.

## Getting Started

To use this script, you need to have Python installed on your machine. You can install the necessary dependencies by running the following command:
```
pip install streamlit openai
```
You also need to replace the placeholder `YOUR-OPENAI-API-KEY` with your actual OpenAI API key. If you don't have an API key, you can sign up for one on the [OpenAI website](https://openai.com/).

## Usage

1. Run the script using the following command:
```
streamlit run app.py
```

2. Open the displayed URL in your web browser. You will see a web interface where you can select meals from different categories (Dinner, Lunch, and Breakfast).

3. After selecting the meals, click on the "Create Grocery List" button to generate a consolidated grocery list. The list will be displayed on the screen, showing the quantity of each item.

4. If you want recipe suggestions based on your grocery list, click on the "Suggest me more recipes" button. The script will use OpenAI's text generation model to provide three recipe suggestions.

Please note that this script uses the Streamlit framework for the web interface and the OpenAI API for recipe suggestions. Make sure to handle user data responsibly and adhere to OpenAI's terms of service and usage guidelines.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.