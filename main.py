# Function to swap three numbers
def swap_three_numbers(a, b, c):
    return c, a, b

# Input from the user
print("Enter three numbers:")
num1 = float(input("First number: "))
num2 = float(input("Second number: "))
num3 = float(input("Third number: "))

# Swapping the numbers
new_num1, new_num2, new_num3 = swap_three_numbers(num1, num2, num3)

# Displaying the swapped numbers
print(f"After swapping: {new_num1}, {new_num2}, {new_num3}")

