#5 inputs
name = input("What is your name?: ")
age = input("How old are you?: ")
gender = input("What is your gender: ")
weight = input("How much do you weigh (in kg?): ")
height = input("How tall are you (in cm)?")

#typecasting into str, int and float

name_string = str(name)
gender_string = str(gender)

age_int = int(age)

weight_float = float(weight)
height_float = float(height)

#print statements

print("Your name is " + name_string)
print(f"You are {age_int} years old. ")
print("You are" + gender_string)
print("Your weight is ", weight_float)
print("Your height is ", height_float)