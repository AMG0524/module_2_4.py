numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers: # перебираем весь список
    if i == 1:    # пропускаем единицу согласно условию
        continue
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(i)
    else:
            not_primes.append(i)

print(primes)
print(not_primes)





