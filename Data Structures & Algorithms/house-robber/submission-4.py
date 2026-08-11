class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for _ in range(2, n):
            dp[_] = max(dp[_ - 1], dp[ _ - 2] + nums[_])
        return dp[-1]