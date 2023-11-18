max_num = -float('inf')

while True:
    num_input = int(input("Enter a number: "))

    if num_input == 0:
        break

    if num_input > max_num:
        max_num = num_input

if max_num != -float('inf'):  
    print(f"The largest input is: {max_num}")
else:
    print("No valid number entered.")
