# simple temperature converter for celcius n farrenheit

unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ").lower()
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = round((9 *temp) / 5 + 32,1)
    unit = 'Fahrenheit'
    print(f"Your converted temperature in fahrenheit is: {temp} degrees {unit}.")

elif unit == "f":
    temp = round((temp - 32) * 5 / 9,1)
    unit = 'Celcius'
    print(f"Your converted temperature in celcius is: {temp} degrees {unit}.")

else:
    print("Invalid unit, please try again!")