#!/usr/bin/python3

# import functools, itertools

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += 1
    return True    

def prime_factorization(n: int) -> list[tuple[int, int]]:
    f = []
    x = 2
    while x * x <= n:
        e = 0
        while n % x == 0:
            n //= x
            e += 1
        if e > 0:
            f.append((x, e))
        x += 1
    if n > 1:
        f.append((n, 1))
    return f

def number_of_factors(n: int) -> int:
    f = prime_factorization(n)
    num_factors = 1
    # ideally I would want to use functool.reduce
    # but it seems tricky...
    for _, e in f:
        num_factors *= e + 1
    return num_factors

def sum_of_factors(n: int) -> int:
    f = prime_factorization(n)
    s = 1
    for prime_factor, e in f:
        s *= (prime_factor ** (e + 1) - 1) // (prime_factor - 1) 
    return s

def product_of_factors(n: int) -> int:
    return n ** (number_of_factors(n) // 2)

def factors(n: int) -> list[int]:
    f = [1]
    x = 2
    while x * x <= n:
        if n % x == 0:
            f.append(x)
        x += 1
    f.append(n)
    return f


if __name__ == '__main__':
    print(is_prime(5))
    print(is_prime(84))
    print(prime_factorization(84))
    print(number_of_factors(84))
    print(sum_of_factors(84))
    print(product_of_factors(84))
    print(factors(84))
    
    
    