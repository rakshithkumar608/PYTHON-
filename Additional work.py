##Let's create a program that classifies a student's grade based on their score:

score_input = input("please enter your score (0-100):")
score = float(score_input)

if score >= 90:
    print("your grade is A")
elif score >= 80:
    print("your grade is B")
elif score >= 70:
    print("your grade is c")
elif score >= 60:
    print("your grade is D")
else:
    print("Invalid score: Score can not be negative")                


##2. Temperature Converter with Weather Advice

celsius_input = input("Please Enter The Temparature in celcius:")
celsius = float(celsius_input)

fahrenheit =  (celsius * 9/5) + 32
print(f"{celsius} * C is equal to {fahrenheit: .1f}°F")

if celsius >= 30:
    print("It's Very hot! Stay hydrated avoid direct sun exposure")

elif celsius >= 20:
    print("It's Warm. Nice weather for outdoor activities!")

elif celsius >= 10:
    print("It's mild. A light jacket might be comfortable")

elif celsius >= 0:
    print("It's cold. wear a worm jacket")

else:
    print("It's freezing! wear warm layers and be careful of ice.")    


##3.Discount Calculator

amount_input = input("Please enter the purchase amount: $")
amount = float(amount_input)

discount_percent = 0

if amount >= 1000:
            discount_percent = 20  # 20% discount for purchases $1000 or more
elif amount >= 500:
            discount_percent = 10  # 10% discount for purchases $500 or more
elif amount >= 200:
            discount_percent = 5   # 5% discount for purchases $200 or more
elif amount < 0:
            print("Error: Purchase amount cannot be negative.")
        
discount = amount * (discount_percent / 100)
final_price = amount - discount        

print(f"Purchase amount: ${amount:.2f}")
print(f"Discount percentage: {discount_percent}%")
print(f"Discount amount: ${discount:.2f}")
print(f"Final price: ${final_price:.2f}")

##4.Bmi calculator

weight_input = input("Please enter your weight in kilograms: ")
height_input = input("Please enter your height in meters: ")
        
weight = float(weight_input)
height = float(height_input)

if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive values.")

              # Calculate BMI
bmi = weight / (height ** 2)
        
        # Display BMI
print(f"Your BMI is: {bmi:.1f}")

if bmi >= 30:
            print("Health category: Obese")
elif bmi >= 25:
            print("Health category: Overweight")
elif bmi >= 18.5:
            print("Health category: Normal weight")
else:
            print("Health category: Underweight")
            
print("\nNote: BMI is a simple screening tool and does not diagnose body fatness or health.")
            