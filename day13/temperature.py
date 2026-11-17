# ASSIGNMENT 2
# Temperature conversion functions between Celsius, Fahrenheit and Kelvin


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    kelvin = celsius + 273.15
    return kelvin


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    celsius = kelvin - 273.15
    return celsius


def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin


def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit


# Testing all conversion functions

print("Celsius to Fahrenheit:", celsius_to_fahrenheit(25))
print("Fahrenheit to Celsius:", fahrenheit_to_celsius(77))

print("Celsius to Kelvin:", celsius_to_kelvin(25))
print("Kelvin to Celsius:", kelvin_to_celsius(298.15))

print("Fahrenheit to Kelvin:", fahrenheit_to_kelvin(77))
print("Kelvin to Fahrenheit:", kelvin_to_fahrenheit(298.15))