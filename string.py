# type:ignore

first_name = "rakshith"
last_name = "gowda"
full_name = first_name + " " + last_name
print(full_name)


#repetetion
message = "This is a Warning!"
print(message*100)

# string meathods
print(message.upper()) #upper
print(message.lower()) #lower
print(message.strip()*3) #strip
print(message.replace("Warning", "Error")) #replace

name = '''rakshith said "Hello!"
         jayanth said "hi"
         '''
print(name)

print(len(message)) #length

#Acessing String Characters
name = "rakshith"
print(name[6]) # index = position - 1
print(name[2:8]) # slicing the string
print(name[:4])  #slicing with left
print(name[6:])  #slicing from right

name = "Rakshith kumar"
print(name[0])
print(name[-3]) #from backword
print(name[-4-3-2-1])

name = "Rakshith"
print(name[::3])

#Escape Sequence

s = "Rakshith \nis a coder" # next line
print(s)

s = "Rakshith \tis a coder" # gives tabs 
print(s)
