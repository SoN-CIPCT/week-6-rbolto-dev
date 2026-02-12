web_users = [ 'Wolverine','Magneto','Mystique','Apocalypse','Juggernaut',]
new_users = [ 'Wolverine','Magneto','Gambit', 'Psylocke','Nightcrawler']

for user in new_users:
    if user in web_users:
        print(f"This user name '{user}' is already in use. please choose a different user name.")
    else:
        print(f"This user name '{user}' is available.")

cities = {}

cities['Kaiserslautern'] = {
    'country': 'Germany',
    'population': 100000,
    'fact': 'Called "Little America because it hosts the largest U.S. military community outside the United States.'


}

cities['Albuquerque'] = {
    'country': 'USA',
    'population': 564559,
    'fact': 'Filming location for the best tv show of all time.'

}

cities['Atlantis'] = {
    'country': 'Ocean Floor',
    'population': 0, 
    'fact': 'Plato made it up.'

}

for city, info in cities.items():
    print(f"{city}: {info['country']}: Population: {info['population']} Fact: {info['fact']}")