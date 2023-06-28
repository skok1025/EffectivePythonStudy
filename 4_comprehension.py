# [better way 27] map과 filter 대신 리스트 컴프리헨션을 사용하라
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for x in a:
    squares.append(x**2)
print(squares)

squares = [x**2 for x in a]
print(squares)

# map 을 사용하면 lambda 를 사용해야한다.
alt = map(lambda x: x**2, a)
print(list(alt))

# 2로 나눠 떨어지는 수에 대해서만 제곱을 계산한다면 이렇게 가능
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

# 물론 filter 와 map 을 사용해도 가능하지만 복잡하다
alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(alt))

even_square_dict = {x: x**2 for x in a if x % 2 == 0}
three_cubed_set = {x**3 for x in a if x % 3 == 0}
print(even_square_dict)
print(three_cubed_set)

# [betterway 28] 컴프리헨션 내부에 제어 하위 식을 세 개 이상 사용하지 말라
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)


# [better way 30] 리스트를 반환하는 대신 제너레이터를 고려하라
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result

address = '컴퓨터(영어: Computer, 문화어: 콤퓨터, 순화어: 전산기)는 진공관'
result = index_words(address)
print(result[0:10])

def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index+1

it = index_words_iter(address)
print(next(it))
print(next(it))

result = list(index_words_iter(address))
print(result[0:10])