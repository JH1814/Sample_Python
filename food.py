from dataclasses import dataclass


@dataclass
class Food: 
    name: str
    calories: float
    protein: float
    carbs: float
    fat: float
    sugar: float

