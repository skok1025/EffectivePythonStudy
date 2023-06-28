# [betterway 84] 모든 함수, 클래스, 모듈에 독스트링을 작성하라

# def 문 바로 다음에 독스트링 추가가능
def palindrome(word):
    """Return True if the given word is a palindrome."""
    return word == word[::-1]

assert palindrome('tacocat')
assert not palindrome('banana')
print(repr(palindrome.__doc__))

# python -m pydoc -p {사용포트}
# => 작성한 모듈을 비롯해 인터프리터에서 찾을 수 있는 모든 파이썬 문서 제공