centuries = int(input())
days_in_one_year = 365.2422
years = 100 * centuries
days = int(years * days_in_one_year)
hours = 24 * days
minutes = 60 * hours

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")
