#1. List Manipulation Exercise:

# Create a list of 5 items (strings or numbers).
# Add a new item to the end of the list and another at the second position.
# Remove the third item from the list.
# Print the list after each operation.

my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(my_list)

my_list.append("fig")
print(my_list)

my_list.insert(1,"grapes")
print(my_list)

my_list.remove("banana")
print(my_list)


#2. Reverse and Sort a List: Create a list of numbers and:

# Sort it in descending order.
# Reverse the sorted list and print it.

my_num = [22,65,34,2,56,89,43,23,12,45]
print(my_num)

my_num.sort()
print(my_num)

my_num.reverse()
print(my_num)