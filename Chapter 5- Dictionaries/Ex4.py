#major river dictionary
major_rivers = {"Nile" : "Egypt", 
                "Yangtze" : "China",
                "Amazon ": "Brazil"}  

#for loop for both key and value inside a print statement
for river, country in major_rivers.items():
    print(f"\nThe {river} runs through {country}")

#River title
print("\nRivers:")

#for loop for the key in major_rivers 
for river in major_rivers.keys():
    print("\t", river)

#countries title
print("\nCountries:")

#for loop for the value in major_rivers
for country in major_rivers.values():
    print("\t", country)