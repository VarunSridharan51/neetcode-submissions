class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}
        l = len (nums)
        for i in range(l):
            diff = target - nums[i]
            if diff in visited:
                return sorted([i, visited[diff]])
            visited[nums[i]] = i