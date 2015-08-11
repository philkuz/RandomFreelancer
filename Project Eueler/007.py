import sys

#performs a sieve of eratosthenes
class Sieve:
    def printSievenum):
        primes = sieve(num)
        counter = 0
        while(counter < num):
            row = 10
            toDisplay = row if num-counter >= row else num-counter
            for i in range(0, toDisplay):
                sys.stdout.write(str(primes[counter])+"\t")
                counter+=1
            print("\n")
    def getPrime(nPos):
        primes = sieve(nPos)
        return primes[-1]
class Eratosthenes(Sieve):
    
def sieve(nth, prev = [2], num = 0):
    primes = prev    
    count = len(primes)
    if(num < primes[-1]):
        num = primes[-1]+1
    pool = range(num, num+1000)
    
    for i in range(0, len(pool)):
        for prime in primes:
            if(pool[i] != 0 and pool[i]%prime == 0):
                pool[i] = 0
    #clear 0s
    iterator = 0;
    while(iterator < len(pool)):
        if(pool[iterator] == 0):
            
            pool.pop(iterator)
        else:
            primes.append(pool[iterator])
            if(len(primes) == nth):
                return primes
            for j in range(iterator, len(pool)):
                if(pool[j]%primes[-1]==0):
                    pool[j] = 0
            iterator+=1
    if(len(primes) < nth):
        primes += sieve(nth, primes, num+1000)
    return primes

def getPrime(nPos):
    primes = sieve(nPos)
    return primes[-1]
print getPrime(10000)


                
    
