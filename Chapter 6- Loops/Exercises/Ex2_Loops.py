#print statement for ticket cost per age
print("""Welcome to the cinema! Here are the following costs of a ticket:
            3 years below is free
            3-12 is $10
            12 above is $15""")

#total cost variable for math operation within the input
total_cost = 0

#while loop for the input
while True:
    ticket_age = input("How old are you?: ")

#if statement that intructs the code to end task
    if ticket_age.lower() == 'quit':
        break
# try variable to instruct the line of code to excecute
    try:

#converting the age input into an integer
        age = int(ticket_age)

#if statement that states the age and its ticket cost
        if age < 3:
            ticket_cost = 0
            print("The ticket is free of charge!")

        elif 3 <= age <= 12:
            ticket_cost = 10
            print("The ticket costs $10")

        else:
            ticket_cost = 15
            print("The ticket is $15")

#looping operation for adding ticket cost per input
        total_cost += ticket_cost

#except element that gives a statement to invalid inputs (non-intregal inputs)
    except ValueError:
        print("Input invalid. enter a valid age.")

#print statement to total ticket cost.
print(f"The total cost of your ticket will be ${total_cost}. Enjoy!")


