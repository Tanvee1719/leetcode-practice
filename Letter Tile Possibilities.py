class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = collections.Counter(tiles)
        
        def dfs(counter) -> int:
            ans = 0
            for k, v in counter.items():
                if v == 0: continue
                counter[k] -= 1
                ans += 1
                ans += dfs(counter)
                counter[k] += 1
            return ans

        return dfs(counter)
        