# CS104
# First name Last name
# conditions.py

# Prompting the user for input
temp = int(input("Please enter the current temperature: "))

# Checking temperature conditions and giving recommendations
if temp > 90:
    print("Wear Shorts")
elif temp > 70:
    print("Short sleeves are fine")
elif temp > 50:
    print("Wear a jacket")
elif temp > 32:
    print("Wear a heavy coat")
else:
    print("Stay Inside")
