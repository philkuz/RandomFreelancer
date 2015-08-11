import time

def isPalinDrome(number):
    palinNum = str(number)
    for i in range(0, len(palinNum)/2):
        if(palinNum[i] != palinNum[-(i+1)]):
            return False
    return True

def highestPalinDrome():
    highestNum = 0;
    start = time.time()
    multiples = []
    for i in range(100, 1000):
        for j in range(100,1000):
            product = i*j;
            if(isPalinDrome(product) and product > highestNum):
                multiples = [i,j]
                highestNum = product;
    end = time.time()-start
    print "Time to process: "+ str(end)
    print "Highest palin drome that is the product of 2 3-digit numbers " +str(highestNum)
    print "The numbers are : " + str(multiples)
    return highestNum
highestPalinDrome()

