self_information = {"Name: ": "John",
                    "Age: ": 17,
                    "Gender: ": "Male"}
favorite_information = {"Animal:": "Dog",
                        "Sport:": "Basketball",
                        "Celebrity:": "Drake"}

merge_information = {**self_information, **favorite_information}

for key, value in merge_information.items():
    print(key, value)