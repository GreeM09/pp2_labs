def FahrenheitToCelsius(F):
    C = (F - 32) * (5 / 9) 
    return C

temperature = FahrenheitToCelsius(float(input("Enter the temperature in Fahrenheit: ")))

print(f"{temperature:.1f} Celsius")
