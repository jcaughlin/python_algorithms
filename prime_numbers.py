import time
import math


def list_prime_numbers(largest_integer):
    prime_number_list = []

    t0 = time.time()
    for num in range(2, 5000):
        max_divisor = math.floor(math.sqrt(num))
        for i in range(2, max_divisor + 1):
            if(num % 2) == 0 or (num % i) == 0:
                break
        else:
            prime_number_list.append(num)
    t1 = time.time()

    calculation_time = 'Time to compute is {}'.format(t1-t0)

    return calculation_time, prime_number_list
