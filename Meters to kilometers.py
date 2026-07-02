try:
    meter = float(input("Enter length in meters: "))
    print(f"Kilometer: {meter / 1000}")
except ValueError:
    print("Error: The entered value is not a valid number.")
