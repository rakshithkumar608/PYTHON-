# Straight pyramid
def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

print_pyramid(5)


# number  pyramid
def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + str(i) * (2 * i - 1))

print_number_pyramid(5)

# Inverted pyramid

# def print_inverted_pyramid(rows):
#     for i in range (rows, 0 , -1):
#         print(' ' * (rows -i ) + '*' * (2 * i - 1))

#         print_inverted_pyramid(5)

def inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

inverted_pyramid(5)


# Inverted number pyramid
def print_inverted_number_pyramid(rows):
    for i in range(rows,0, -1 ):
        print(' ' * (rows - i) + str(i) * (2 * i - 1))
print_inverted_number_pyramid(5)

# Hollow pyramid
def print_hollow_pyramid(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print(' ' * (rows - i) + '*' * (2 * i - 1))
        else:
            print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + '*')

print_hollow_pyramid(5)

# Hollow inverted pyramid
def print_hollow_inverted_pyramid(rows):
    for i in range(rows, 0, -1):
        if i == 1 or i == rows:
            print(' ' * (rows - i) + '*' * (2 * i - 1))
        else:
            print(' ' * (rows - i) + '*' + ' ' * (2 * i - 3) + '*')

print_hollow_inverted_pyramid(5)


# Hollow number pyramid
def print_hollow_number_pyramid(rows):
    for i in range(1, rows + 1):
        if i == 1 or i == rows:
            print(' ' * (rows - i) + str(i) * (2 * i - 1))
        else:
            print(' ' * (rows - i) + str(i) + ' ' * (2 * i - 3) + str(i))

print_hollow_number_pyramid(5)

# Full pyramid-2

def print_full_pyramid(rows):
    for i in range(1, rows +1):
        print(' ' * (rows - i), end='')
        print('*' * (2 * i - 1))

print_full_pyramid(5)

# full number pyramid-2
def print_full_number_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i), end='')
        print(str(i) * (2 * i - 1))

print_full_number_pyramid(5)