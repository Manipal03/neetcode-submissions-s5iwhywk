class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer=[]
        for x in range(2):
            for y in nums:
                answer.append(y)
        return answer
        
        