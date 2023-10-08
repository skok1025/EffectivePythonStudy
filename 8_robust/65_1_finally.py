def try_finally_example(file_name: str):
    print("file read start")
    handle = open(file_name, encoding='utf-8')  # IOError 발생 가능

    try:
        print("file read try")
        return handle.read()  # UnicodeDecodeError 발생 가능
    finally:
        print("file close call")
        handle.close()  # try 블록에서 예외가 발생하든 안하든 항상 실행

file_name = "test.txt"

with open(file_name, 'wb') as f:
    f.write(b'\xf1\xf2\xf3\xf4\xf5')

data = try_finally_example(file_name)