from functools import lru_cache
import time


def main():
    begin = time.time()
    print(begin)

    for n in range(1, 250):
        print(n, ":", fibonacci(n))

    end = time.time()
    print(end)

    print(end-begin)


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    main()
