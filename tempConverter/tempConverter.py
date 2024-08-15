def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_c = float(input("Enter the celsius temperature: "))
temp_f = celsius_to_fahrenheit(temp_c)

print(f"{temp_c} degrees celsius is equal to {temp_f} degrees fahrenheit")
