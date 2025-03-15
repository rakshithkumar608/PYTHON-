## Input

print("Love")

boy_name = input("Boy Name: ")
boy_age =  int (input("Boy Age: "))
girl_name = input("Girl Name: ")
girl_age = int (input("Girl Age: "))

## using abs because sometimes boy might be younger
age_diff = abs(boy_age - girl_age)

print(boy_name + " loves " + girl_name + ". Age Difference is " + str(age_diff)) ##Concatenation

print(f"{boy_name} loves {girl_name}. Age Difference is {age_diff}")##formatted string