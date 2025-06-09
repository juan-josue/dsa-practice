from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # { 'alice': [['happy', 1], ['sad', 3] ] }
        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Binary search to find the highest (most recent) time less than the given timestamp
        res = ""
        vals = self.d.get(key, [])
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
