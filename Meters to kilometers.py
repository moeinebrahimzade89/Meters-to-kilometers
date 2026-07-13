print("Select Convert. 1.Meters to kilometers  2.Kilometer to meter")
Choose = input("Choose:")
try:
    meter = float(input("meter:"))
except ValueError:
    print("Error: The entered value is not a valid number.")

if Choose == '1':
    print("Kilometer:",meter / 1000)
elif Choose == '2':
    print("meter:",meter * 1000)
