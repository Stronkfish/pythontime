main = input("Stronkfish Brand Temperature Converter\n\nCLS = Convert to Celsius\nFHR = Convert to Fahrenheit\n\n") # Choose Conversion CLS or FHR (1)
conv = "" # Pre-Define (2)
if main.upper() == "CLS": # CLS to FHR Conversion (3-5)
    conv = float(input("\nEnter the Temperature in Celsius to convert it into Fahrenheit: "))
    print(f"\nCelsius: {conv} \nFahrenheit: {conv*9/5+32}")
if main.upper() == "FHR": # FHR to CLS Conversion (6-8)
    conv = float(input("\nEnter the Temperature in Fahrenheit to convert it into Celsius: "))
    print(f"\nFahrenheit: {conv} \nCelsius: {(conv-32)*5/9}")
