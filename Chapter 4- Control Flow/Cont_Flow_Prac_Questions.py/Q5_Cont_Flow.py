month_seasons = input("What is the month right now? (number): ")

month_number = int(month_seasons)

if month_number in (1, 2):
    season = 'Spring'
elif month_number in (3, 4, 5, 6, 7, 8):
    season = 'Summer'
elif month_number in (9, 10):
    season = 'Autumn'
elif month_number in (11, 12):
    season = 'Winter'
else:
    season = 'That does not belong in the calendar months!'

print(f"The season will be {season}")