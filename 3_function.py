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


# better way 22 변수 위치 인자를 사용해 시각적인 잡을을 줄여라
def log(message, values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{message}: {value_str}')

log('My numbers are', [1, 2])
log('Hi there', []) # 2번째 인자가 빈 리스트임에도 넘겨줘야함

def log(message, *values):
    if not values:
        print(message)
    else:
        value_str = ', '.join(str(x) for x in values)
        print(f'{message}: {value_str}')
log('My numbers are', 1, 2)
log('Hi there')

# * 연산자를 사용하면 제너레이터의 모든 원소를 얻기 위해 반복한다는 뜻입니다.
# 이로 인헤 메모리를 아주 많이 소비하거나 프로그램이 중단돼버릴수도 있다.

def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)
# *args 를 받는 부분의 인자의 개수가 충분히 작다는 사실을 이미 알고 있는 경우에 적합하다.
# 그렇지 않으면 메모리를 많이 소비하거나 프로그램이 중단될 수 있다.

# better way 23 키워드 인자로 선택적인 기능을 제공하라
def remainder(number, divisor):
    return number % divisor
assert remainder(20, 7) == 6

# 키워드인자를 넘기는 순서는 관계없다
remainder(20,7)
remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 위치 기반 인자를 지정하려면 키워드 인자보다 앞에 지정해야한다.
#remainder(number=20, 7) # SyntaxError: positional argument follows keyword argument

# **연산자를 이용하면 딕셔너리로도 파라미터 넘길 수 있음 (개인적인 생각: 굳이??)
my_kwargs = {
    'number': 20,
    'divisor': 7,
}
assert remainder(**my_kwargs) == 6


# 함수에 아무 인자나 받고 싶을때 **kwargs 를 사용한다.
def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')

print_parameters(alpha=1.5, beta=9, 감마=4, kim=123)
