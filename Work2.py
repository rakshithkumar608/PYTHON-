# Work1 

#1.Simple Greeting Program: Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.

#boy_name = input("Enter your Name: ")
#boy_age = int(input("Enter your Age: "))

#print(f"Hello, {boy_name}! You are {boy_age} year old.")

#2.String Manipulation Exercise: Write a Python program that:

#Takes a sentence as input from the user.
#Prints the sentence in all uppercase and lowercase.
#Replaces all spaces with underscores.
#Removes leading and trailing whitespace

message = "  Python is awesome! "
print(message*10)

print(message.upper())
print(message.lower())
print(message.replace("Python is awesome!", "__python_is_awesome!___"))
print(message.strip()*4)

#3.Character Counter: Write a Python program that:

# Asks the user for a string.
#Prints how many characters are in the string, excluding spaces.
name = "Hello World"
print(len(name)) #including space = 11
print (len(name.replace(" ", ""))) #Excluding space = 10


#4.Escape Sequence Practice: Write a Python program that uses escape sequences to print the following output:

greeting = "Hello \nWorld"
print(greeting) 

g = "Hello \tWorld"
print(g)