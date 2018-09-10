class Solution:
    # @return a float
    def kth(self, A, B, k):
        la = len(A)
        lb = len(B)
        if la == 0:
            return B[k-1]
        if lb == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])
        if la > lb:
            return self.kth(B,A,k)
        i = min(la, k/2)
        j = k - i
        if A[i-1] == B[j-1]:
            return A[i-1]
        elif A[i-1] > B[j-1]:
            return self.kth(A, B[j:lb], k-j)
        else:
            return self.kth(A[i:la], B, k-i)

    def findMedianSortedArrays(self, A, B):
        la = len(A)
        lb = len(B)
        if (la + lb) % 2 == 1:
            return self.kth(A,B,(la+lb+1)/2)
        else:
            return (self.kth(A,B,(la+lb)/2) + self.kth(A,B,(la+lb)/2+1))/2.0


if __name__ == "__main__":
    A = [1, 2]
    B = [3, 4]
    print Solution().findMedianSortedArrays(A, B)
