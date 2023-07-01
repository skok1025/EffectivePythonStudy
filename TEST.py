fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5
}

# 대입식을 사용하면 더 간결하게 표현할 수 있다.
if count := fresh_fruit.get('레몬', 0):
    print('make_lemonade')
else:
    print('out_of_stock')

print(count)