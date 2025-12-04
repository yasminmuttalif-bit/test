#list
fruits = ["apple", "banana", "cherry"]  #same data
numbers = [1, 2, 3, 4, 5]               #same data
mixed = ["Hello", 42, 2.5, True]        #different data types
empty_list = []                           #empty list for add database later on

# # Accessing elements
# print(fruits[0])  # start from the 1st data in data set 
# print(fruits[-1]) # last data in data set
# print(numbers[1:3])  # slice from index 1 to 2
# print(numbers[:3])   # slice from start to index 2
# print(numbers[2:])   # slice from index 2 to end

#List operation: Crud_a_list
# fruits.append("orange")           #add data to the end of the list
# fruits.insert(1, "kiwi")          #add data at specific index
# fruits.remove("banana")           #remove specific data
# popped = fruits.pop()               #remove and return last data in popped variable
# fruits.sort()                     #sort in place
# fruits.reverse()                  #reverse in place

# List of operations
# len(fruits)         #length of the list
# "apple" in fruits   #check if "apple" is in the list
result = fruits + ["mango"]  #concatenate lists    
# result = fruits * 2          #repeat list

# print(len(fruits))
# print(fruits)
# print(popped)
print(result)

                    