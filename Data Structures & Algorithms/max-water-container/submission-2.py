class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_store = 0
        left, right = 0, len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_store = max(area, max_store)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_store