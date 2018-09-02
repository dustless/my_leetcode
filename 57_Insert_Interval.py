# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        if len(intervals) == 0:
            return [newInterval]
        intervals.sort(lambda i1,i2: cmp(i1.start, i2.start))
        i = 0
        while i < len(intervals) and newInterval.start > intervals[i].start:
            i += 1
        j = max(i-1, 0)
        if j == 0 and intervals[0].start >= newInterval.start:
            if intervals[0].start <= newInterval.end <= intervals[0].end:
                intervals[0] = Interval(newInterval.start, intervals[0].end)
                return intervals
            elif newInterval.end < intervals[0].start:
                intervals.append(newInterval)
                intervals.sort(lambda i1,i2: cmp(i1.start, i2.start))
                return intervals
        if intervals[j].end >= newInterval.end:
            return intervals
        if j < len(intervals)-1 and intervals[j].end < newInterval.start and newInterval.end < intervals[j+1].start:
            intervals.append(newInterval)
            intervals.sort(lambda i1,i2: cmp(i1.start, i2.start))
            return intervals

        if j == 0 and intervals[j].start > newInterval.start:
            start = newInterval.start
        elif intervals[j].end < newInterval.start:
            if j == len(intervals) - 1:
                intervals.append(newInterval)
            j += 1
            start = newInterval.start
        else:
            start = intervals[j].start
        while j < len(intervals) and newInterval.end > intervals[j].start:
            if j == len(intervals) - 1:
                intervals.append(Interval(start, max(newInterval.end, intervals[j].end)))
                intervals.pop(j)
                break
            elif newInterval.end <= intervals[j].end:
                intervals[j] = Interval(start, intervals[j].end)
                break
            elif newInterval.end < intervals[j+1].start:
                intervals[j] = Interval(start, newInterval.end)
            elif newInterval.end == intervals[j+1].start:
                intervals[j] = Interval(start, intervals[j+1].end)
                intervals.pop(j+1)
            else:
                intervals.pop(j)
        return intervals

if __name__ == '__main__':
    solution = Solution()
    intervals = [
        Interval(1,5),
        Interval(6,8)
    ]
    newInterval = Interval(5,6)
    print solution.insert(intervals, newInterval)