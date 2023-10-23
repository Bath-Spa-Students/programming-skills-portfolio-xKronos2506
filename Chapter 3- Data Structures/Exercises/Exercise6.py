# CHANGE NAME OF ONE GUEST AND REPLACE WITH ANOTHER

# guest list
guest_name = ['Tupac Shakur', 'Duterte', 'Eminem', 'Eriel', 'Biggie Smalls']

# Loop to invite all guests
for guest in guest_name:
    print(f"Greetings! Mr. {guest}, you are invited to my dinner!")

# Sir Tupac unfortunately had an issue
remove_guest = "Tupac Shakur"
print(f"\nUnfortunately, Mr {remove_guest} cannot make it to dinner!\n")

# Replace it with Mr. Juice WRLD
new_guest = "Juice WRLD"

#use if replacing the removed guest with new guest in its index
remove_guest = guest_name[0]
guest_name[0] = new_guest

print(f"Greetings! {new_guest}, you are invited to my dinner!")

# pop off guests that are not invited, combine with print message
print(f"Unfortunately Mr. {guest_name.pop(4)}, due to the lack of available reservations you are not invited to dinner due to limited seats.")
print(f"Unfortunately Mr. {guest_name.pop(2)}, due to the lack of available reservations you are not invited to dinner due to limited seats.")
print(f"Unfortunately Mr. {guest_name.pop(1)}, due to the lack of available reservations you are not invited to dinner due to limited seats.")
# message the remaining guests invited
for invited_guests in guest_name:
    print(f"Fortunately, Mr. {invited_guests}, you are still invited to the dinner")
# use del to remove
del guest_name[1]
del guest_name[0]
#print list with no more element
print(guest_name)