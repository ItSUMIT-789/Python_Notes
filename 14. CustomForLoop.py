fruits = iter(['apple', 'orange', 'banana', 'guava'])

#  we are using her a try and except
while True:
    try:
        element = next(fruits)
        print(element)
    except StopIteration:
        break