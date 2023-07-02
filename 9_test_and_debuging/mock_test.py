from datetime import datetime
from unittest.mock import Mock, ANY


class DatabaseConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port

def get_animals(database, species):
    # (이름, 급양 시간) 튜플의 리스트를 반환한다.
    return [('동물1', '급양시간1'), ('동물2', '급양시간2')]

database = DatabaseConnection('localhost', 8080)

mock = Mock(spec=get_animals)
expected = [
    ('점박이', datetime(2020, 6, 5, 11, 15)),
    ('털보', datetime(2020, 6, 5, 12, 30)),
    ('조조', datetime(2020, 6, 5, 12, 45)),
]

mock.return_value = expected
print(mock.return_value)
print(mock(database, '고양이'))

mock.assert_called_once_with(database, '고양이')
#mock.assert_called_once_with(database, '강아지')
# AssertionError: expected call not found.
# Expected: mock(<__main__.DatabaseConnection object at 0x00000198EBB47DC0>, '강아지')
# Actual: mock(<__main__.DatabaseConnection object at 0x00000198EBB47DC0>, '고양이')

mock.assert_called_with(ANY, '고양이')


# 예외발생 Mock 테스트
class MyError(Exception):
    pass

mock = Mock(spec=get_animals)
mock.side_effect = MyError('테스트용 오류')
result = mock(database, '고양이')
