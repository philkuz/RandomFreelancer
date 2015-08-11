#iterative approach
def nextFibo(a = [1,2]):
    if len(a) != 2:
        print "ERROR, there should only be two numbers as input"
    return [a[1],a[0]+a[1]]
def iterative(limit):
    evenFibs = [2]
    curRecurse = nextFibo([1,2])
    while curRecurse[-1] < limit:
        
        if(curRecurse[1]%2 == 0):
            evenFibs.append(curRecurse[1])
        curRecurse = nextFibo(curRecurse)
    evenSums = 0
    for fib in evenFibs:
        evenSums+=fib
    print evenFibs
    return evenSums
def sqrt(n):
    return n**(.5)
def closedFibo(a = 0):
    return int(1/sqrt(5.0)*(((1+sqrt(5.0))/2.0)**a- ((1-sqrt(5.0))/2)**a))
def closedForm(limit):
    curFib = closedFibo()
    count = 0
    evenSums = 0
    evenFibs = []
    while(curFib <  limit):
        if(curFib%2 == 0):
            evenFibs.append(curFib)
            evenSums+=curFib

        count+=1
        curFib = closedFibo(count)
    print evenFibs
    return evenSums
