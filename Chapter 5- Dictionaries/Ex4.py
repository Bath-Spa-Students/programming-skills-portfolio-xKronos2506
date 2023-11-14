#major river dictionary
major_rivers = {"Nile" : "Egypt", 
                "Yangtze" : "China",
                "Amazon ": "Brazil"}  

#for loop for both key and value inside a print statement
for river, country in major_rivers.items():
    print(f"\nThe {river} runs through {country}")

print("\nRivers:")

for river in major_rivers.keys():
    print("\t", river)

print("\nCountries:")

for country in major_rivers.values():
    print("\t", country)