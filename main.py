from matplotlib import pyplot as plt
from food import Food
import numpy as np

Day = [] 

while True:
    print(
        """
        Welcome to the Nutrition Tracker!
        you have these options:
        1. Add Food Item
        2. View Summary
        3. Exit
        """
    )

    selected_option = input("Select an option (1-3): ")
    if selected_option == "1":
        name = input("Enter food name: ")
        calories = float(input("Enter calories: "))
        protein = float(input("Enter protein (g): "))
        carbs = float(input("Enter carbs (g): "))
        fat = float(input("Enter fat (g): "))
        sugar = float(input("Enter sugar (g): "))

        food_item = Food(name, calories, protein, carbs, fat, sugar)
        Day.append(food_item)
        print(Day)
        print(f"Added {food_item.name} with {food_item.calories} calories.")

    elif selected_option == "2":

        total_calories = sum(item.calories for item in Day)
        total_protein = sum(item.protein for item in Day)
        total_carbs = sum(item.carbs for item in Day)
        total_fat = sum(item.fat for item in Day)
        total_sugar = sum(item.sugar for item in Day)

        fig, ax = plt.subplots(2,2)
        fig.suptitle("Nutrition Summary")

        ax.pie(
            [total_protein, total_carbs, total_fat],
            labels=["Protein", "Carbs", "Fat"],
            autopct="%1.1f%%",
        )
        ax.set_title("Total Intake")


        plt.savefig("nutrition_summary.png")
        plt.tight_layout()
        plt.show()
