class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        #result = [1,1,2,8]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]
        #result = [48,24,12,8]
        return result