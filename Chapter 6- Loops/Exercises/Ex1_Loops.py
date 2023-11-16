#pizza toppings list (contains the follwing input in toppings variable)
pizza_toppings = []

#while loop for the input. Loops whenever an input is recieved.
while True:
    toppings = input("What will be your pizza toppings? ")
#break variable, which instructs the code to end if "quit" is inputed
    if toppings == 'quit':
        break
    pizza_toppings.append(toppings)


for toppings in pizza_toppings:
    print(f"\n This are the following pizza toppings you chose: {toppings} ")

