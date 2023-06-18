# slice
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('가운데 2개', a[3:5])

assert a[:5] == a[0:5]

b = a[:]
assert b == a and b is not a
print(b == a)
print(b is not a)

car_age = [0, 9, 4, 10, 20, 1, 3, 4]
car_age_descending = sorted(car_age, reverse=True)

oldest, second_oldest, *other = car_age_descending

print(oldest, second_oldest, other)

car_ages = [0, 4, 10, 26, 37]
car_ages_descending = sorted(car_ages, reverse=True)
print(car_ages_descending)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest)

numbers = [93, 86, 11, 68, 70]

numbers.sort()
print(numbers)

class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'

tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('chisel', 0.25)
]

tools.sort(key=lambda x: x.name)
print(tools)

places = ['home', 'work', 'New York', 'Paris']
places.sort()
print(places)

places.sort(key=lambda x: x.lower())
print(places)
