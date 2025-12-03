name = input("Enter your name:")
height = float(input("Enter your height:"))

# Input validation
while True:
    try:
        age = int(input("Enter your age:"))
        if age > 0:
            break
        else:
            print("Please enter a valid positive age!")
    except ValueError:
        print("Invalid input. Please enter a number for your age!")


# Output validation
print(f"Hello, {name}!") 
print(f"You are {age} years old and {height} feet")
