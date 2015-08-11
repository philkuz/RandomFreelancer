#The iterative way
multiples = []
for i in range(0,1000):
    if (i%3) == 0 or (i%5)== 0:
        multiples.append(i)
sum = 0;
for num in multiples:
    sum += num;

print "The iteraive solution: "+str(sum);
#the algebraic solution
def sum_simplify(n):
    return .5 * n * (n+1)
def multiples(limit = 1000, nums = [3,5]):
    limit -= 1
    occurrences = []
    for num in nums:
        #should be the lower bound of the division
        print "num: "+ str(limit/num)
        occurrences.append(limit/num);        
    #conflict handling
    mults = []
    for i in range(0,len(nums)):
        for j in range(1, len(nums)):
            if(i == j):
                continue
            else:
                mults.append(nums[i]*nums[j])
    mult_occur = []
    for mult in mults:
        print "mult: "+ str(limit/mult)
        mult_occur.append(limit/mult)

    output_sum = 0
    for i in range(0, len(nums)):
        output_sum+=nums[i]*sum_simplify(occurrences[i])
    for j in range(0, len(mults)):
        output_sum-=mults[j]*sum_simplify(mult_occur[j])
    print "The algebraic solution: " + str(output_sum)
multiples(1000)
