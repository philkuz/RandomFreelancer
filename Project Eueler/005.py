def highestMultiple(num):
    multiples = list(range(2,num))
    print multiples
    for i in range(0, len(multiples)):
        cur = multiples[i]
        print "Getting multiple " + str(i) + " : " + str(multiples)
        for j in range(i+1, len(multiples)):
            splorer = multiples[j]
            if(splorer%cur == 0):
                multiples[j]/=cur
    print multiples
    product = 1
    for multiple in multiples:
        product*=multiple
    return product
print highestMultiple(20)
