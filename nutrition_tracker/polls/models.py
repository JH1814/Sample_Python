from django.db import models

class Food(model.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    sugar = models.FloatField()
    meal_type = models.CharField(max_length=20, choices=[("Breakfast", "Breakfast"), ("Lunch", "Lunch"), ("Dinner", "Dinner"), ("Snack", "Snack")], default="Breakfast")

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # In a real app, use Django's built-in User model and hashing
    weight = models.FloatField()  # in kg
    height = models.FloatField()  # in cm
    age = models.IntegerField()
    

