
def sieve(limit):
    res = []
    if limit >1 : res.append(2)
    # we only should check the odd numbers.
    for i in range(3, limit+1, 2) :
        if isprime(i) : res.append(i)
    return res

def isprime(n) :
    if n ==2 or n ==3 : return True
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0 : return False
    return True

