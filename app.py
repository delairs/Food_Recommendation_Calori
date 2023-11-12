from flask import Flask, render_template
import random
from constraint import Problem

app = Flask(__name__)

def food_recommendation(daily_calories, food_dict):
    problem = Problem()
    for food in food_dict:
        problem.addVariable(food, range(int(daily_calories / food_dict[food]) + 1))

    problem.addConstraint(lambda *foods: sum(food*food_dict[food_name] for food, food_name in zip(foods, food_dict)) == daily_calories, food_dict.keys())

    solutions = problem.getSolutions()

    if solutions:
        return random.choice(solutions)
    else:
        return None

# Example dictionary of foods with calories
food_dict = {
    "Nasi": 200,
    "Ayam Goreng": 250,
    "Sayur Asem": 100,
    "Tahu": 50,
    "Tempe": 150
}

daily_calories = 1000

@app.route('/')
def index():
    # Call food_recommendation within the index function
    recommended_food = food_recommendation(daily_calories, food_dict)

    # Pass the result to the render_template function
    return render_template('index.html', recommended_food=recommended_food)

if __name__ == '__main__':
    app.run(debug=True)
