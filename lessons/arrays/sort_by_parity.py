class Solution(object):
    def sortArrayByParity(self, A):
        A.sort(key=lambda x: x % 2)
        return A


class Solution(object):
    def sortArrayByParity(self, A):
        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])


class Solution(object):
    def sortArrayByParity(self, A):
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]

            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1

        return A
