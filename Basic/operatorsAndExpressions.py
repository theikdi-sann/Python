# 3. Operators & Expressions

# Exercise 3.1: Area of a Rectangle
# Prompt the user to enter the length and width of a rectangle.
# Calculate and print its area.
# Also, calculate and print its perimeter.

# Exercise 3.2: Temperature Converter (Celsius to Fahrenheit)
# Ask the user to input a temperature in Celsius.
# Convert it to Fahrenheit using the formula: F=C×(9/5)+32.
# Print the converted temperature.

from abc import abstractmethod, ABC


class Promptable(ABC):
    @abstractmethod
    def prompt_user_input(self):
        pass


class AreaOfRectangle(Promptable):
    def __init__(self):
        self.prompt_user_input()

    def prompt_user_input(self):
        self.length = float(input("Enter length of Rectangle: "))
        self.width = float(input("Enter width of Rectangle: "))

    def calculate(self):
        return self.length * self.width

    def __str__(self):
        return f"The area of rectangle: {self.calculate()}"


class TemperatureConverter(Promptable):
    def __init__(self):
        self.prompt_user_input()

    def prompt_user_input(self):
        self.temperature = float(input("Enter Temperature: "))
        self.unit = input("Enter Unit: ")

    def convert(self):
        if self.unit.lower() == "f":
            return f"Temperature in C: {(self.temperature - 32) * 5 / 9}"
        elif self.unit.lower() == "c":
            return f"Temperature in F: {(self.temperature * 9 / 5) + 32}"
        else:
            return "Invalid Temperature Unit!"

    def __str__(self):
        return self.convert()


temperature_converter = TemperatureConverter()
print(temperature_converter)

area_of_rectangle = AreaOfRectangle()
print(area_of_rectangle)
