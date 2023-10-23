# CHANGE NAME OF ONE GUEST AND REPLACE WITH ANOTHER

# guest list
guest_name = ['Tupac Shakur',  'Duterte', 'Eminem', 'Eriel', 'Biggie Smalls']

#for loop in guest list
for guest_name in guest_name:
    print(f"Greetings! {guest_name}, you are invited to my dinner!")


# Sir Tupac unfortunately had an issue
remove_guest = "Tupac Shakur"
print(f"\nUnfortunately, Mr {remove_guest} cannot make it to dinner!\n")

# replace it with mr Juice WRLD
new_guest = "Juice WRLD"

print(f"Greetings! {new_guest}, you are invited to my dinner!")
