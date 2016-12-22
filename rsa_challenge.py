import math
import random
import requests
from fractions import gcd

def getRandInts():
    link = "https://www.random.org/integers/?num=10000&min=1&max=255&col=1&base=10&format=plain&rnd=new"
    r = requests.get(link).text
    r = r.encode("ascii", "ignore")
    r = r.split()
    randlist = [int(num) for num in r]
    #randlist = my_randoms=[random.randrange(1,255,1) for _ in range (10000)]
    return randlist


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2- temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in xrange(3, int(n**0.5)+2, 2):
        if n % i == 0:
            return False
    return True


def getPrimeRandom(min, max):
    p = math.floor(random.randint(1,255) * (max - min)) + min
    if is_prime(p):
        return int(p)
    else:
        return getPrimeRandom(min, max)

def generateKeypair():
    p, q = None, None

    while 1:
        x = getPrimeRandom(1, 255)
        y = getPrimeRandom(1, 255)
        if x == y:
            continue
        else:
            p, q = int(x), int(y)
            break

    n = p * q

    phi = (p-1) * (q-1)

    e = getRandInts()
    e = e[:phi]
    e = e[2]

    g = gcd(e, phi)
    while g != 1:
        e = getRandInts()
        e = e[:phi]
        e = e[2]
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)

    return ((e, n), (d, n))

print generateKeypair()