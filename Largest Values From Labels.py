class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        limit = collections.defaultdict(int)
        nodes = sorted(zip(values, labels))
        ans = 0
        while nodes and num_wanted:
            value, label = nodes.pop()
            if limit[label] < use_limit:
                ans += value
                limit[label] += 1
                num_wanted -= 1
        return ans
        