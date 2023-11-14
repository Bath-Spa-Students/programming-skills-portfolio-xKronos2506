#pet dictionary, consists of pet name and owner name:
pets_dicts_1 = {"Pet": "German Shepherd Dog", "Owner Name": "Chaewon"}
pets_dicts_2 = {"Pet": "British Shorthair Cat", "Owner Name": "Yunjin"}
pets_dicts_3 = {"Pet": "Cockatiel", "Owner Name": "Hanni"}
pets_dicts_4 = {"Pet": "Chinese Striped Hamster", "Owner Name": "Danielle"}

pets_lists = [pets_dicts_1, pets_dicts_2, pets_dicts_3, pets_dicts_4]

for pets in pets_lists:
    print(f"Pet Breed and Animal Name: {pets['Pet']}")
    print(f"Owner Name: {pets['Owner Name']}\n")
