#lists

items = ["Bru", "Sugar", "Milk", "Chicken"]
print(items)
print(len(items))

items.pop(0)  #it removes the first element
print(items)

items.append("Eggs") #it adds the element at the end
print(items)

items.remove("Sugar") # it removes the element
print(items)

items.insert(1, "spoon") #it adds the element at the specified index
print(items)

items[0] = "coffee powder" #it replaces the element at the specified index
print(items)

#items.clear() #it clears the list
#print(items)


#print(items[0]) = Bru
#print(items[-1]) = prints from reverse
#print(items[2]) = milk
#print(items[3]) = chicken

## Slicing the list

#list_name = [start:stop:step]

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  # Output: [1, 2, 3] (from index 1 to 3)
print(numbers[:4])  # Output: [0, 1, 2, 3] (from start to index 3)
print(numbers[2:])  # Output: [2, 3, 4, 5, 6] (from index 2 to end)
print(numbers[::2])  # Output: [0, 2, 4, 6] (every 2nd element)

# Common functoins in lists

numbers = [100, 82, 57, 43, 57, 6]

sorted_numbers = sorted(numbers)  # Returns a new sorted list
print(sorted_numbers)

#reverse_sorted_numbers = sorted(numbers, reverse=True)  # Returns a new reverse sorted list
#print(reverse_sorted_numbers)

print(numbers.count(57))  # Output: 2

print(numbers.index(43))  # Output: 3

numbers.reverse()  # Reverses the list in place
print(numbers)


# Nested Lists

m = [[1,2], [3,4]]

print(type(m[0][1]))