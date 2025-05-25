# Exercise 1: Simple Calculator
# Ask the user to enter two numbers.
# Convert the input strings to appropriate numeric types (integers or floats).
# Calculate and print their sum, difference, product, and quotient.

# Exercise 2: Favorite Thing
# Ask the user for their favorite color and their favorite animal.
# Print a sentence that combines these two inputs, for example: "My favorite combination is a [color] [animal]!"

# Exercise 1
class SimpleCalculator:
    _instance = None

    # Singleton
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        return "You can't divide by Zero"


# Exercise 2
class FavoriteThings:
    def __init__(self, color, animal):
        self.color = color
        self.animal = animal

    def __str__(self):
        return f"My favourite combination is a {self.color} {self.animal}!"


calc1 = SimpleCalculator()
calc2 = SimpleCalculator()


def calculate(num1, num2, operator):
    if "+".__eq__(operator):
        print(calc1.add(num1, num2))
    elif "-".__eq__(operator):
        print(calc1.subtract(num1, num2))
    elif "*".__eq__(operator):
        print(calc1.multiply(num1, num2))
    elif "/".__eq__(operator):
        print(calc1.divide(num1, num2))
    else:
        print("Invalid Operator")


num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operator = input("Enter Operator: ")

calculate(num1, num2, operator)

print(f"Singleton Check: {calc2 is calc1}")

color = input("Enter your favourite color: ")
animal = input("Enter your favourite animal: ")

fav = FavoriteThings(color, animal)
print(fav)
