# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        dic = {}
        max_result = 0
        i = 0
        j = 0
        l = len(points)
        if l <= 2:
            return l
        points_weight = {}
        u_points = []
        for i in range(0, l):
            key = "%s_%s" % (points[i].x, points[i].y)
            if key not in points_weight:
                points_weight[key] = 1
                u_points.append(points[i])
            else:
                points_weight[key] += 1

        ul = len(u_points)

        for i in range(0, ul):
            for j in range(j + 1, ul):
                key_i = "%s_%s" % (u_points[i].x, u_points[i].y)
                key_j = "%s_%s" % (u_points[j].x, u_points[j].y)
                if u_points[i].x == u_points[j].x:
                    if "inf" in dic:
                        dic["inf"] = dic["inf"].union(set([key_i, key_j]))
                    else:
                        dic["inf"] = set([key_i, key_j])
                else:
                    slope = float(u_points[i].y - u_points[j].y)/float(u_points[i].x - u_points[j].x)
                    if slope in dic:
                        dic[slope] = dic[slope].union(set([key_i, key_j]))
                    else:
                        dic[slope] = set([key_i, key_j])
        max_points = 0
        for key_set in dic.values():
            points = 0
            for key in key_set:
                points += points_weight[key]
            if points > max_points:
                max_points = points
        return max_points


if __name__ == '__main__':
    solution = Solution()
    points = []
    param = [[1,1],[1,1],[1,1],[2,2],[2,2],[3,3]]
    for param_p in param:
        points.append(Point(param_p[0], param_p[1]))
    print solution.maxPoints(points)