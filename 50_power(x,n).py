# class Solution:
#     # @param {float} x
#     # @param {integer} n
#     # @return {float}
#     def myPow(self, x, n):
#         if n < 0:
#             return 1.0/self.myPow(x, -n)
#
#         xn = [1.0, x]
#         i = 1
#         result = 1.0
#         while n > 0:
#             if n % 2 == 1:
#                 result *= xn[i]
#             xn.append(xn[i]*xn[i])
#             i += 1
#             n >>= 1
#         return result




# class __deco():
#     dic = {}
#     def __init__(self, func):
#         print "init dic"
#         self.dic = {}
#         self.func = func
#
#     def __call__(self, x, n):
#         print "in decorator"
#         if n in self.dic:
#             print "in dic"
#             return self.dic[n]
#         else:
#             result = self.func(self, x, n)
#             print "not in dic"
#             print self.dic
#             print n
#             self.dic[n] = result
#             print self.dic
#             return result
# @__deco
# def pow(self, x, n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return x
#     mid_value = self.pow(x, n/2)
#     if n % 2 == 0:
#         return mid_value*mid_value
#     else:
#         return mid_value*mid_value*x

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    dic = {}
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n in self.dic:
            return self.dic[n]
        mid_value = self.myPow(x, n/2)
        if n % 2 == 0:
            result = mid_value*mid_value
            self.dic[n] = result
            return result
        else:
            result = mid_value*mid_value*x
            self.dic[n] = result
            return result


if __name__ == '__main__':
    x = 2
    n = 12
    solution = Solution()
    print solution.myPow(x, n)