import math

# Input: Get the coefficients of the quadratic equation (ax^2 + bx + c)
a, b, c = map(float, input("Enter the coefficients (space-separated) a b c: ").split())

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check the nature of roots
if discriminant > 0:
    # Real and different roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are real and different:\nRoot1 = {root1}\nRoot2 = {root2}")
elif discriminant == 0:
    # Real and same roots
    root = -b / (2*a)
    print(f"Roots are real and the same:\nRoot = {root}")
else:
    # Imaginary roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Roots are imaginary:\nRoot1 = {real_part} + {imaginary_part}i\nRoot2 = {real_part} - {imaginary_part}i")
