import math
# variables
cash = 50
price = 6

# amount of usb sticks that can be bought

amnt = cash//price

print("The girl can buy",amnt, "pieces worth of usb sticks")

#amount of change left from buying USB sticks
# calculate amount used + change

used_money = amnt * price
change = cash - used_money

print(used_money)
print("The girl has change worth",change ,"pounds")