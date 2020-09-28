class Solution:
    def replaceElements(self, arr: List[int], mx=-1) -> List[int]:
        for i in range(len(arr) - 1, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr
