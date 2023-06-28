import itertools

# C 스타일 str 포맷팅의 문제점
key = 'my_var'
values = 1.234
formatted = '%-10s = %.2f' % (key, values)

print(formatted)

#formatted2 = '%-10s = %.2f' % (values, key) # TypeError: must be real number, not str
# 1) 순서가 중요함.

# ===================== 해결 내용
new_way = '%(key)-10s = %(value).2f' %{'key': key, 'value': values}
new_way = '%(key)-10s = %(value).2f' %{'value': values, 'key': key}
print(new_way)

pantry = [
    ('아보카도', 1.25),
    ('바나나', 2.5),
    ('체리', 15),
]

for i, (item, count) in enumerate(pantry): # 2) 가독성이 떨어짐
    print('#%d: %-10s = %.2f' % (
        i+1,
        item.title(),
        round(count)
    ))
    print(f'#{i+1}: {item.title():<10s} = {round(count):.2f}')

# 3) 같은값을 사용하려면 반복해서 써야함
template = '%s 는 음식을 좋아해. %s가 요리하는 모습을 봐요.'
name = '철수'
formatted = template % (name, name)
print(formatted)

# ===================== 해결 내용
template = '%(name)s 는 음식을 좋아해. %(name)s가 요리하는 모습을 봐요.' % {'name': '철수'}
print(template)

menu = {
    'soup': 'lentil',
    'oyster': 'tongyoung',
    'special': 'schnitzel'
}

template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters '
            'and our special entree is %(special)s.')

formatted = template % menu

template = ('Today\'s soup is {soup}s, '
            'buy one get two {oyster}s oysters '
            'and our special entree is {special}s.')

formatted2 = template.format(soup='entile', oyster='tongyoung', special='scsc')
print(formatted)
print(formatted2)


a = 1234.5678
formatted = format(a, ',.2f')
print(formatted)

b = 'my 문자열'
formatted = format(b, '^20s')
print('*', formatted, '*')

key = 'my_bar'
value = 1.234

formatted = '{} = {}'.format(key, value)
print(formatted)

key = 'my_var'
value = 1.234
formatted = f'{key} = {value}'
print(formatted)

formatted = f'{key:<10} = {value: .2f}'
print(formatted)

names = ['Cecilia', 'Lise', 'Marie']
count = [len(n) for n in names] # list comprehension
print(count)

max_count = 0
names.append('Rosalind')
for name, name_count in zip(names, count):
    print(name, name_count)
    if name_count > max_count:
       longest_name = name
       max_count = name_count

print(longest_name, max_count)


for name, name_count in itertools.zip_longest(names, count):
    print(name, name_count)


for i in range(3):
   print(i)
else:
   print('done')


for i in range(3):
   print(i)
   if i == 1:
      break
else:
    print('done')


fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5,
}

count = fresh_fruit.get('바나나', 0)
if count >= 4:
    print('바나나 4개 이상')


if (count2 := fresh_fruit.get('바나나', 0)) >= 4:
    print('바나나 4개 이상')

a = b'h\x65llo'
print(list(a))
print(a)
a = 'a\u0300 propos'
print(list(a))
print(a)