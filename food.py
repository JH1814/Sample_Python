from dataclasses import dataclass


@dataclass
class Food: 
    name: str
    calories: float
    protein: float
    carbs: float
    fat: float
    sugar: float
    meal_type: str = "Breakfast", "Lunch", "Dinner", "Snack"  # Default meal type
    date: str = "YYYY-MM-DD"   # Default date format