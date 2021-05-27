class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = preSum = 0
        seen = {}
        for i, h in enumerate(hours):
            preSum = preSum + 1 if h > 8 else preSum - 1
            if preSum > 0:
                ans = i + 1
            seen.setdefault(preSum, i)
            if preSum - 1 in seen:
                ans = max(ans, i - seen[preSum - 1])
        return ans
        