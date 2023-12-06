def convert_temperature(temp, direction):
    
    if direction == 'F_to_C':
        # Convert from Fahrenheit to Celsius
        return (temp - 32) * 5 / 9
    elif direction == 'C_to_F':
        # Convert from Celsius to Fahrenheit
        return temp * 9 / 5 + 32
    else:
        # Invalid direction
        return None

celsius = float(input("Please enter the Celsius value: "))
fahrenheit = float(input("Please enter the Fahrenheit value: "))

celsius_to_fahrenheit = convert_temperature(celsius, 'C_to_F')
fahrenheit_to_celsius = convert_temperature(fahrenheit, 'F_to_C')

print(f"The fahrenheit value of {celsius} is: {celsius_to_fahrenheit:.2f}")
print(f"The celsius value of {fahrenheit} is: {fahrenheit_to_celsius:.2f}")
