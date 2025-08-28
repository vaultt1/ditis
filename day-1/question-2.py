# 2. Write a Python Program to Convert Celsius To Fahrenheit vice versa.
# Fahrenheit to Celsius: °C = (°F - 32) × 5/9
# Celsius to Fahrenheit: °F = (°C × 9/5) + 32

choice= int(input("""Enter your choice: 
1. Enter 1 for Celsius To Fahrenheit
2. Enter 2 for Fahrenheit to Celsius
"""))

if choice==1:
    fahrenheit_to_celsius()
else:
    celsius_to_fahrenheit()
    
    
def fahrenheit_to_celsius():
    temp=int(input("Enter Temperature in Fahrenheit:    "))
    celsius = (temp-32)*(5/9)
    print(f"Temperature in Celsius is: {celsius}°C ")

def celsius_to_fahrenheit():
    temp=int(input("Enter Temperature in Celsius:    "))
    fahrenheit = (temp*(5/9)+32)
    print(f"Temperature in Celsius is: {fahrenheit}°F ")

