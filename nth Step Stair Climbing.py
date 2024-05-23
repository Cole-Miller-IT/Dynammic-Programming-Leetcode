class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        elif n == 2:
            return 2
        
        else:
            #n > 2
            #for n > 2 the amount of solutions will be  S(n) = S(n - 1) + S(n - 2)
            #Init base cases
            n1 = 1
            n2 = 2
            n3 = -1
            
            #Compute the nth number of solutions
            for step in range(n - 2):
                #print(step)
            
                n3 = n1 + n2
                
                n1 = n2
                n2 = n3
                
            return n3