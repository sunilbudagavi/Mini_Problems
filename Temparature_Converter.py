def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def temperature_converter(value, unit):
    if unit.lower() == 'c':
        celsius = float(value)
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
        return fahrenheit, kelvin
    elif unit.lower() == 'f':
        fahrenheit = float(value)
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
        return celsius, kelvin
    elif unit.lower() == 'k':
        kelvin = float(value)
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
        return celsius, fahrenheit
    else:
        return "Invalid unit. Please use 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin."

# Example usage:
value = input("Enter the temperature value: ")
unit = input("Enter the temperature unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")

converted_temperatures = temperature_converter
