#pet dictionary, consists of pet name and owner name:
pets_dicts_1 = {"Pet": "German Shepherd Dog", "Owner Name": "Chaewon"}
pets_dicts_2 = {"Pet": "British Shorthair Cat", "Owner Name": "Yunjin"}
pets_dicts_3 = {"Pet": "Cockatiel", "Owner Name": "Hanni"}
pets_dicts_4 = {"Pet": "Chinese Striped Hamster", "Owner Name": "Danielle"}

#all dictionaries concatenated into a list called pet_list
pets_lists = [pets_dicts_1, pets_dicts_2, pets_dicts_3, pets_dicts_4]

#for loop from the pet_list 
for pets in pets_lists:
#print statement for both pet name and owner name within the pet_list variable.
    print(f"Pet Breed and Animal Name: {pets['Pet']}")
    print(f"Owner Name: {pets['Owner Name']}\n")
