from unittest import TestCase, main
from utils import to_str

class UtilTestCase(TestCase):
    def test_to_str_bytes(self):
        self.assertEqual('hello', to_str(b'hello'))

    def test_to_str_str(self):
        self.assertEqual('hello', to_str('hello'))

    def test_failing(self):
        self.assertNotEquals('incorrect', to_str('hello'))

    def test_to_str_bad(self):
        with self.assertRaises(TypeError): # 에러가 발생할 것이다라는걸 테스트
            to_str(object())

if __name__ == '__main__':
    main()