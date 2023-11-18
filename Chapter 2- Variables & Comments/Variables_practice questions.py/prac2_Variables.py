#input for grades in each subject
science_grades = int(input("What is your grade in Science?: "))
math_grades = int(input("What is your grade in Math?: "))
english_grades = int(input("What is your grade in English: "))
social_science_grades = int(input("What is your grade in Social Science? :"))

#adding a variable which adds all inputs in total sum
sum_grade = science_grades + math_grades + english_grades + social_science_grades

#adding a variable which gets the average grade by dividing the sum by the number of subjects.
average_grade = sum_grade // 4

print(f"Your grade average in total will be: {average_grade}")
