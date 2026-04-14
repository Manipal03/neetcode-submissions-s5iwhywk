class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans=0
        for x in range(len(nums)):
            if nums[x]!=val:
                nums[ans]=nums[x]
                ans=ans+1
        return ans