class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        #answer[i] == "Fizz" if i is divisible by 3.
        #answer[i] == "Buzz" if i is divisible by 5.
        #answer[i] == i (as a string) if none of the above conditions are true.
        answer = [0 for number in range(n)]
        i = 0
        for number in range(1, n + 1):
            #print("current number: " + str(number))
            msg = ""
            
            if (number % 3) == 0:
                msg = msg + "Fizz"
                
            if (number % 5) == 0:
                msg = msg + "Buzz"
                
            if msg == "":
                msg = str(number)
                
                
            #print(msg)
            answer[i] = msg
            
            i += 1
            
        return answer