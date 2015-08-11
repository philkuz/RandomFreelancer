#iterative way
class SumsBase:
    def __init__(self, num = 10):
        self.iterations = num
    def squareOfSum(self):
        iterations  = self.iterations +1
        retSum = sum(i for i in range(0,iterations))
        return retSum**2
    def difference(self):
        print "Sum of squares: "+ str(self.sumOfSquares())
        print "Square of sum: " + str(self.squareOfSum())
        return self.squareOfSum()- self.sumOfSquares() 
class Iterative(SumsBase):
    
    def sumOfSquares(self):
        iterations  = self.iterations+1
        retSum = 0;
        for i in range(0,iterations):
            retSum+= i**2;
        return retSum
    
class Algebraic(SumsBase):
    #(n)(n+1)/2
    def sumOfSquares(self):
        iterations = self.iterations
        return iterations*(iterations+1)*(2*iterations+1)/6
        
    
cur = Iterative(100)
print cur.difference()
cur = Algebraic(100)
print cur.difference()
