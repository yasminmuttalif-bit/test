# name = input("Enter your name:")
# height = float(input("Enter your height:"))

# # Input validation
# while True:
#     try:
#         age = int(input("Enter your age:"))
#         if age > 0:
#             break
#         else:
#             print("Please enter a valid positive age!")
#     except ValueError:
#         print("Invalid input. Please enter a number for your age!")


# # Output validation
# print(f"Hello, {name}!") 
# print(f"You are {age} years old and {height} feet")


# #excercise
# Question_1 = input ("1+1 =")
# Question_2 = input ("what is the capital of France?")
# Question_3 = input ("what is 5*6?")
# Score = 0
#input validation

    
# answer_1 = int(input ("1+1 ="))
# if answer_1 == 2:
#     Score += 1
# else:
#     print("Aha! Wrong, try again.")

    
# answer_2 = str(input ("what is the capital of France?"))
# if answer_2.lower() == "paris":
#     Score += 1
    
# else:
#     print("Aha! Wrong, try again.")
  
       

# answer_3 = int(input ("what is 5*6?"))
# if answer_3 == 30:
#     Score += 1

# else:
#     print("Aha! Wrong, try again.")
   
    
#     #output validation
# print("Congratulations! You answered all questions correctly.")
# print("1+1 =", answer_1)
# print("The capital of France is", answer_2)
# print("5*6 =", answer_3)


# Conditional_statement

# age = 18
# age = int(input("Enter your age:"))
# if age>= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote yet.")


# Score = 20
# if Score >= 90:
#     grade = "A+"
# elif Score >= 80:
#     grade = "A"
# elif Score >= 75:
#     grade = "A-"
# elif Score >= 65:
#     grade = "B+"
# elif Score >= 60:
#     grade = "B"
# elif Score >= 50:
#     grade = "C"
# else:
#     grade = "D"

# print(f"Your grade is: {grade}")


# user_age = 17
# has_license = True
# if user_age >= 18 and has_license:
#     print("You are allowed to drive.")
# else:
#     print("You are not allowed to drive.")


# day="Monday"
# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("It's a weekday.")

#excercise BMI_calculator
# weight = float(input("Enter your weight in kg:"))
# height = float(input("Enter your height in meters:"))
# BMI = weight / (height ** 2)
# print(f"Your BMI is: {BMI:.2f}")
# if BMI < 18.5:
#     category = "Underweight"
# elif 18.5 <= BMI < 24.9:
#     category = "Normal weight"
# elif 25 <= BMI < 29.9:
#     category = "Overweight"
# else:
#     category = "Obesity"
# print(f"You are categorized as: {category}")



# loops
#for_loops

# for i in range(5):
#     print(i)
# for i in range(1, 6):
#     print(i)
# for i in range(1, 10, 3):
#     print(i)

# while_loops
# count = 0
# while count < 5:
#     print(count)
#     count+=1 

# loop_control_statements

# for i in range (18):
#     if i == 10:
#         continue
#     if i == 15:
#         break            #Exit theloop
#     print(i)

# nested_loop
# for i in range(2):
#     for j in range(3):
#         print(f"({i}, {j})")

# excercise_multiplication_table

# num = int(input("Enter a number to generate its multiplication table:"))
# print(f"Multiplication table for {num}:")
# for i in range(1, 13):
#     product = num * i
#     print(f"{num} x {i} = {product}")

# excercise_find_prime_numbers
limit = int(input("Find prime numbers up to:"))
print(f"Prime numbers up to {limit}:")
for num in range(2, limit + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)