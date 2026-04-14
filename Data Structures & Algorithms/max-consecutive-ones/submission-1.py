class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mymax=0
        cur=0
        for x in nums:
            if x!=0:
                cur+=1
                mymax=max(mymax, cur)
            else:
                cur=0
        return mymax