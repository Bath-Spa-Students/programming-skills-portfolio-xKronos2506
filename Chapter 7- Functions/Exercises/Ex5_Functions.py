#"descibe_city()" as a function with "city" and "country" as parameter
def descibe_city(city="Tokyo", country="Japan"):
    print(f"The city of {city} is in {country}")

#calling a default parameter function
descibe_city()

#calling the function with the modified "city" parameter
descibe_city(city="Kyoto")
descibe_city(city="Okinawa")

#calling the function with both parameter modified
descibe_city(city="Moscow", country="Russia")

