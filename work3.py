## Logical operators

a = 34
b = 23

print(a > 30 and b < 20)
print(a > 39 or b > 25)
print(not(b < 21))


## comparision Operator

age_input = input("please enter your age:")
age = int(age_input)

if age >= 18:
    print("you are an Adult")
elif age < 18:
    print("you are a minor")

#Membership Operator

my_list = [1, 3, 4, 6 ]
my_string = "python"

print(5 in my_list)
print("a" in my_string )
print("python" not in my_string)

#Bitwise Operator

p = 20
q = 10

print(p&q)
print(p|q)
print(p^q)
print(p<<10)
print(q>>20)