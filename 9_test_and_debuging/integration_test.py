from unittest import TestCase, main

def setUpModule():
    print('setUpModule')

def tearDownModule():
    print('tearDownModule')

class IntegrationTest(TestCase):
    def setUp(self) -> None:
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_end_to_end1(self):
        print('test_end_to_end1')

    def test_end_to_end2(self):
        print('test_end_to_end2')

if __name__ == '__main__':
    main()