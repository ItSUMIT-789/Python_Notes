# Collections is a libray: Counters, namedTuple

# 1) Counter
from collections import Counter

randomString = 'sdfgcuahdgiuyrghbagjfuhaguyirygbvagbvaorbgajgfj'#counts how mant a element has been countered
my_counter = Counter(randomString)
print(my_counter.most_common())
print(my_counter.most_common(5)) # will return only fifth result


# 2) NamedTuple
from collections import namedtuple

Details = namedtuple('College', ('studentname', 'id', 'result'))
user1 = Details('abc', '125', 'fail')
print(user1)


