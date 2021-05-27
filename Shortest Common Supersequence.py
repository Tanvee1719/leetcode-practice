class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        def longestCommonSubSeq(str1: str, str2: str) -> str:
            dp = [[""] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key = len)
            return dp[m][n]
        
        ans, p1, p2 = "", 0, 0
        for c in longestCommonSubSeq(str1, str2):
            while p1 < m and str1[p1] != c:
                ans += str1[p1]
                p1 += 1
            while p2 < n and str2[p2] != c:
                ans += str2[p2]
                p2 += 1
            ans += c
            p1, p2 = p1 + 1, p2 + 1
        return ans + str1[p1:] + str2[p2:]
        