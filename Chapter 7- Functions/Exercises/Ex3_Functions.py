#make_shirt() as a function with "message" and "size" as its parameter
def make_shirt(message, size):
#print statement for both parameters
    print(f"{message} {size}")

#calling a function using positional argument
make_shirt("I love Kanye", "medium")

#calling a function using keyword argument
make_shirt(message="I love Kanye",size="medium")