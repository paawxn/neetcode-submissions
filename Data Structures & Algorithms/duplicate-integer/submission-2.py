class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setS = set()
        for i in nums:
           setS.add(i)
        
        if len(setS)<len(nums): return True
        else: return False