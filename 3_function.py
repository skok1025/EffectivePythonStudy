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


# [better way 22] 변수 위치 인자를 사용해 시각적인 잡을을 줄여라
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

# [better way 23] 키워드 인자로 선택적인 기능을 제공하라
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

from time import sleep
from datetime import datetime
# [better way 24] None 과 독스트링을 사용해 동적인 디폴트 인자를 지정하라

# 함수의 디폴트 값은 모듈이 로드되는 시점에 딱 한번만 평가된다.
# 그래서 아래 when 은 값은 값이 들어감. 함수가 호출될때마다 계속 같은 값이 들어간다.
def log(message, when=datetime.now()):
    print(f'{when}: {message}')

log('Hi there!')
sleep(0.1)
log('Hi again!')


def log(message, when=None):
    """
    Log a message with a timestamp.
    :param message:
    :param when: 메세지가 발생한 시각(datetime) 디폴트값은 현재시각이다.
    :return:
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

log('Hi there!')
sleep(0.1)
log('Hi again!')

import json

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1

# foo 와 bar 가 같은 딕셔너리를 참조한다.
print('Foo:', foo) # Foo: {'stuff': 5, 'meep': 1}
print('Bar:', bar) # Bar: {'stuff': 5, 'meep': 1}

assert foo is bar

def decode(data, default=None):
    """
    Load JSON data from a string.
    :param data: JSON data to decode
    :param default: Value to return if decoding fails.
    :return:
    """
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default

foo = decode('bad data')
foo['stuff'] = 5
bar = decode('also bad')
bar['meep'] = 1
print('Foo:', foo) # Foo: {'stuff': 5}
print('Bar:', bar) # Bar: {'meep': 1}
assert foo is not bar

from typing import Optional
def log_typed(message: str,
              when: Optional[datetime] = datetime.now()) -> None:
    """
    Log a message with a timestamp.
    :param message:
    :param when:
    :return:
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

# [better way 25] 위치로만 인자를 지정하게 하거나 키워드로만 인자를 지정하게 해서 함수 호출을 명확하게 만들라

def safe_division(number, divisor, ignore_overflow=False, igore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if igore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division(1.0, 10**500, True, False)
print(result) # 0.0

result = safe_division(1.0, 0, False, True)
print(result) # inf

result = safe_division(1.0, 10**500, ignore_overflow=True)
print(result) # 0

# * 기호는 위치 인자의 마지막과 키워드만 사용하는 인자의 시작을 구분해준다.
def safe_division_c(number, divisor, *,
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise
#safe_division_c(1.0, 10**500, True, False) # TypeError: safe_division_c() takes 2 positional arguments but 4 were given

# [better way 26] functools.wraps 를 사용해 함수 데코레이터를 정의하라

from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r})'
              f' -> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """Return the n-th Fibonacci number"""
    if n in (0,1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))

fibonacci(4)
print(fibonacci) # <function trace.<locals>.wrapper at 0x0000020F4F4F1D08>