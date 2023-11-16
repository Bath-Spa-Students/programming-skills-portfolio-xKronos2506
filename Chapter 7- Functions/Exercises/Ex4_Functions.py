#defining make_shirt() function with a proper parameter message.
def make_shirt( message="I love Python", size="Large"):
    print(f"T-Shirt message: {message} T-Shirt size: {size}")

#calling the function with its default parameter
make_shirt()

#calling a function with its modified size parameter
make_shirt(size="Medium")

#calling a function with both parameters modified
make_shirt(message="Python is my bae <3", size="Small")
