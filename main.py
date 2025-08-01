def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("Choose input scale:")
    print("1. Celsius\n2. Fahrenheit\n3. Kelvin")
    choice = int(input("Enter choice (1/2/3): "))
    
    temp = float(input("Enter the temperature: "))

    if choice == 1:
        print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
        print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
    elif choice == 2:
        print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
        print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")
    elif choice == 3:
        print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
        print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

