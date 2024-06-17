class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arrayLength = len(prices)
        
        if arrayLength == 0:
            return 0
        
        elif arrayLength == 1:
            return 0
        
        else:
            #length 2 or greater
            curBuyPrice = 999999    #large int number or max integer
            profit = 0              #must be 0
            
            for price in prices:
                #determine the lowest buy price
                if price < curBuyPrice:
                    curBuyPrice = price

                else:
                    #see if this price gives a better profit
                    potentialReturn = (price - curBuyPrice)
                    if potentialReturn > profit:
                        profit = potentialReturn
            
            
            return profit