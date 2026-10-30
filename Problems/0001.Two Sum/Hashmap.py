class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hashmap solution
        seen={}

        for idx,val in enumerate(nums):
            remaining=target-val

            if remaining in seen:
                return [seen[remaining],idx]
            
            seen[val]=idx
        
