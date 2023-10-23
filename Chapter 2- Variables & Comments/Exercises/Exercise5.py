import math
# variables
cash = 50
price = 6

# amount of usb sticks that can be bought

usb = cash//price

print("The girl can buy", usb, "pounds worth of usb sticks")

#amount of change left from buying USB sticks
# calculate amount used + change

used_money = usb * price
change = cash - used_money

print("THe girl used ", used_money, "pounds")
print("The girl has change worth", change ,"pounds")