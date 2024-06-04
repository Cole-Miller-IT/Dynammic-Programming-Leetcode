class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        else:
            #2 or more numbers in the array
            house = [0 for x in range(length)] #create an array to hold all of the values
            #Get base cases
            house[0] = nums[0]
            house[1] = max(nums[0], nums[1])
            
            #Loop for all of the houses
            i = 2
            while(i < length):
                #take the best choice of the next house + all previous houses or the previous houses
                house[i] = max(nums[i] + house[i - 2], house[i - 1])
                
                i += 1
            
            
            return house[length - 1]