## Using a Temporary Variable

a = 5
b = 10

print(f"Before swap: a = {a}, b = {b}")

temp = a
a  = b 
b = temp

print(f"After swap: a = {a}, b = {b}")

## Without Using a Temporary Variable

a = 5
b = 10

print(f"Before swap: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swap: a = {a}, b = {b}")

## Using Python Tuple Unpacking(Most Pythonic Way)

x = "hello"
y = "Rakshith"

print(f"Before swap: x = {x}, y = {y}")

x, y = y, x

print(f"After swap: x = {x}, y = {y}")


## Using Arithmetic Operations(for Nuymbers Only)

m = 100
n = 200

print(f"Before swap: m = {m}, n = {n}")

m =  m + n
n = m - n
m = m - n

print(f"After swap: m = {m}, n = {n}")


## Using XOR Bitwise Operator

p = 1000
q = 2000

print(f"Before swap: p = {p}, q = {q}")

p = p ^ q
q = p ^ q
p = p ^ q

print(f"After swap: p = {p}, q = {q}")

## Using Division and Multiplication

x = 10000
y = 20000

print(f"Before swap: x = {x}, y = {y}")

x = x / y
y = x * y
x = y / x

print(f"After swap: x = {x}, y = {y}")

## Using Python List Unpacking

a = 100000
b = 200000

print(f"Before swap: a = {a}, b = {b}")

[a, b] = [b, a]

print(f"After swap: a = {a}, b = {b}")




##Swapping List Elements

my_list = [1, 2, 3, 4, 5]
print(f"original list: {my_list}")

my_list[0], my_list[4] = my_list[4], my_list[0]

print(f"Swapped list: {my_list}")