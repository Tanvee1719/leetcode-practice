class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        dp = [False] * (s // 2 + 1)
        dp[0] = True
        for i in range(len(stones)):
            for j in range(s >> 1, stones[i] - 1, -1):
                dp[j] |= dp[j - stones[i]]
        return min(s - i - i for i in range(s // 2 + 1) if dp[i])
        