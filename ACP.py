# Import the math module to get the value of pi
import math

# Function to calculate the circumference
def circumference(radius):
    return 2 * math.pi * radius

# Ask the user for input
r = float(input("Enter the radius of the circle: "))

# Calculate and display the circumference
print("The circumference of the circle is:", circumference(r))
