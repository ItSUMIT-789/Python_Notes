# The Zip Function :
'''
# Takes Iterable (lists, tuples, dictionaries, strings)
# is used for parallel iteration
# returns a zip object which is an iterator of tuples

'''


# 1) LISTS useing for loop

countries = ['India', 'Australia', 'America', 'United Kingdom']
capitals = ['Delhi', 'Sydney', 'Washington D.C']
cities = ['city1', 'city2', 'city3', 'city4']

# for index in range(0, 4):
#     country = countries[index]
#     capital = capitals[index]
#     print(f' Country : {country}  Capital : {capital}')


# 2) Zip function   

# for country, capital, city in zip(countries, capitals, cities):
#     print(20, country, capital, city)

# for country in countries:
#     print(f' Country : {country}  Capital : {capital}')

# for capital in capitals:
#     print(capital)



# 3) ZIP Longest

from itertools import zip_longest

countries = ['India', 'Australia', 'America', 'United Kingdom']
capitals = ['Delhi']
cities = ['city1']

for country, capital, city in zip_longest(countries, capitals, cities, fillvalue='N/A'):
    print(country, capital, city )
    # if country == None or capital == None or city == None:
    #     print(country, capital, city )




