import random

class Solution:

    def __init__(self, nums: List[int]):
        self.curArrayLength = len(nums)
        
        self.curArray = nums
        self.availableValues = nums.copy()
        self.nextArray = []

    #uses the old stored array in available values to reset the array
    def reset(self) -> List[int]:
        self.curArray = self.availableValues.copy()
        return self.curArray

    def shuffle(self) -> List[int]:
        #print("===============================")
        iteration = 1
        i = 0
        
        shuffling = True
        while(shuffling):
            if iteration > self.curArrayLength:  
                #reset for next shuffle/reset
                self.availableValues = self.curArray.copy() #Store the previous array to be used by reset()
                self.curArray = self.nextArray.copy()
                self.nextArray = []
                
                #print("after shuffle reset")
                #print("curarray" + str(self.curArray))
                #print("nextArray " + str(self.nextArray))
                #print("available values " + str(self.availableValues))
                #print("===============")
                
                shuffling = False
                break
              
            else:
                #Chose a random value from the available numbers
                chosenIndex = random.randint(0, self.curArrayLength - iteration)
                chosenNumber = self.availableValues[chosenIndex]
                
                #assign it to the array
                self.nextArray.append(chosenNumber)
                
                #remove the value from the pool of available numbers for next round
                self.availableValues.remove(chosenNumber)
            
            i += 1
            iteration += 1
            
        return self.curArray
            
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()