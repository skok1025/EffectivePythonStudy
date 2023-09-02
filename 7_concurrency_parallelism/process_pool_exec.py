import concurrent.futures

def my_function(x):
    return x * x

data = [1, 2, 3, 4, 5]


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(my_function, data))

    print(results)


if __name__ == '__main__':
    main()