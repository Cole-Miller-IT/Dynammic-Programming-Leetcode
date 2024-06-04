class Solution:
    #geeksforgeeks.org/largest-sum-contiguous-subarray/ helped with this and provides a good diagram of what this does
    def maxSubArray(self, nums: List[int]) -> int:
        arrayLen = len(nums)
        
        if arrayLen == 0:
            return 0
        
        elif arrayLen == 1:
            return nums[0]
        
        else:
            #2 or more elements in nums

            maxSum = -1000000
            curMaxSum = 0
            #Find greatest sum
            i = 0
            while(i < arrayLen):
                #Determine the next greatest subarray
                curMaxSum = curMaxSum + nums[i]
                
                #Check if the curMaxSum is now higher than the previous maxSum
                #If the current sum is 0 any positive number would be an increase. If the array(nums) went 4 -> -1 -> -2 -> 1, then the result would be 4-1-2+1=2 so a decrease. Therefore you wouldn't take it.
                if maxSum < curMaxSum:
                    maxSum = curMaxSum
                    
                #resets if curMaxSum becomes negative, this is used to check if finding a positive number after a string of negative numbers/positive numbers would result in an overall increase in the subarray or not. 
                if curMaxSum < 0:
                    curMaxSum = 0
                        
                
                #print("Current greatest subarray found:")
                #print(maxSum)
                i += 1
                
            return maxSum
                