def find_primes(n):

    primes = []
    for num in range(2, n+1):
        for i in primes:
            if num % i == 0:
                break
        else:        
            primes.append(num)

    return primes

print(find_primes(20))