def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)

    return minimum, maximum

lengths = [63, 73, 71, 68, 69, 75, 79, 69, 72, 78]

min, max = get_stats(lengths)
print(f'Min: {min}, Max: {max}')

def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

print(get_avg_ratio(lengths))

longest, *middle, shortest = get_avg_ratio(lengths)
print(f'Longest: {longest:>4.0%}')
print(f'Shortest: {shortest:>4.0%}')


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('Invalid inputs')


def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return ValueError('Invalid inputs')

x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('Invalid inputs')
else:
    print(f'Result is {result:.1f}')