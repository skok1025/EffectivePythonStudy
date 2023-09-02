from concurrent.futures import ProcessPoolExecutor

def my_function(x):
    return x * x

data = [1, 2, 3, 4, 5]

with ProcessPoolExecutor() as executor:
    results = list(executor.map(my_function, data))
ㅐㄱ
print(results)
