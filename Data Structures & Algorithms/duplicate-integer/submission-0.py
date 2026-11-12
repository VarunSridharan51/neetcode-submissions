class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        l = len(nums)
        visited = {}
        for i in range(l):
            if nums[i] in visited:
                return True

            visited[nums[i]] = i
        return False