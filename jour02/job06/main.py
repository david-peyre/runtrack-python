def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Affiche les nombres premiers jusqu'à 1000
primes = [num for num in range(2, 1001) if prime(num)]
print(primes)
