class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        sol = []
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                sol.append(hashmap.get(target - nums[i]))
                sol.append(i)
                return sol
            hashmap[nums[i]] = i
