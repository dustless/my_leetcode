# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort(lambda i1,i2: cmp(i1.start, i2.start))
        i = 0
        while i < len(intervals) - 1:
            if intervals[i].end >= intervals[i+1].start:
                if intervals[i].end < intervals[i+1].end:
                    intervals[i] = Interval(intervals[i].start, intervals[i+1].end)
                intervals.pop(i+1)
            else:
                i += 1
        return intervals


if __name__ == '__main__':
    solution = Solution()
    intervals = [
        Interval(2,6),
        Interval(1,3),
        Interval(8,10)
    ]
    print solution.merge(intervals)