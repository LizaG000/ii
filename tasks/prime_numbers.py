def isPrime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def genPrime(currentPrime):
    newPrime = currentPrime + 1
    while True:
        if not isPrime(newPrime):
            newPrime += 1
        else:
            break
    return newPrime

currentPrime = 2

while True:
    answer = input('Показать следующее простое число? (Y/N) ')
    if answer.lower().startswith('y'):
        print(currentPrime)
        currentPrime = genPrime(currentPrime)
    else:
        break