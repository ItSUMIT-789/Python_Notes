# Syntax : lambda arguments : expression

sub = lambda var1, var2 : var1 - var2
print(sub(20, 10))


# sorting through index
economy = {'india':5000, 'usa':2000, 'srilanka':1000, 'italy':4500}
sorted_economy = dict(sorted(economy.items(), key= lambda  item : item[1]))
#                             ^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^^^^^^^^^
#                             iterable          function
print(sorted_economy)