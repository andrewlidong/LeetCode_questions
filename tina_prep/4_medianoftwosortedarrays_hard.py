class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.mergeSortedArrays(nums1, nums2)
        return self.findMedianSortedArray(merged)

# Time: O(N1 + n2) for the creating of the merged array
# Space: O(N1 + N2) for the size of the merged array

# Input: array nums1, array nums2 -> Output: median of the two sorted arrays
# merge the two sorted arrays and then find the median.
# insertion into a heap is logn.  Thus, we can insert both into a heap, O(nlogn) + O(mlogm) for each element though is the problem...
# I think that's a fine brute force solution to come up with, and then we can keep track of what the length of the heap is.

# probably build a helper for finding the median of a sorted array.

# to merge two sorted arrays
# create an array of size nums1 + nums2
# simultaneously traverse nums1 and nums2
# pick smaller of current elements, copy this smaller element to next position in nums1+nums2 and move ahead in the nums1+nums2 and whichever arrays element was picked
# if there are remaining elements, copy them also into nums1+nums2

    def mergeSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        mergedArrays = [None] * (n1 + n2)

        # Traverse both arrays
        i, j, k = 0, 0, 0
        while i < n1 and j < n2:
            # check if current element of first array is smaller than current element of second array. If so, stored first array element and increment first array index.  Otherwise, do same with second array
            if nums1[i] < nums2[j]:
                mergedArrays[k] = nums1[i]class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = self.mergeSortedArrays(nums1, nums2)
        return self.findMedianSortedArray(merged)

# Time: O(N1 + n2) for the creating of the merged array
# Space: O(N1 + N2) for the size of the merged array

# Input: array nums1, array nums2 -> Output: median of the two sorted arrays
# merge the two sorted arrays and then find the median.
# insertion into a heap is logn.  Thus, we can insert both into a heap, O(nlogn) + O(mlogm) for each element though is the problem...
# I think that's a fine brute force solution to come up with, and then we can keep track of what the length of the heap is.

# probably build a helper for finding the median of a sorted array.

# to merge two sorted arrays
# create an array of size nums1 + nums2
# simultaneously traverse nums1 and nums2
# pick smaller of current elements, copy this smaller element to next position in nums1+nums2 and move ahead in the nums1+nums2 and whichever arrays element was picked
# if there are remaining elements, copy them also into nums1+nums2

    def mergeSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        mergedArrays = [None] * (n1 + n2)

        # Traverse both arrays
        i, j, k = 0, 0, 0
        while i < n1 and j < n2:
            # check if current element of first array is smaller than current element of second array. If so, stored first array element and increment first array index.  Otherwise, do same with second array
            if nums1[i] < nums2[j]:
                mergedArrays[k] = nums1[i]
                k += 1
                i += 1
            else:
                mergedArrays[k] = nums2[j]
                k += 1
                j += 1

        # Store remaining elements of first array
        while i < n1:
            mergedArrays[k] = nums1[i]
            k += 1
            i += 1

        # Store remaining elements of second array
        while j < n2:
            mergedArrays[k] = nums2[j]
            k += 1
            j += 1

        return mergedArrays

# Time: O(N1 + N2)
# Space: O(N1 + N2)

# to find the median, calculate the length, and then find the element at the middle, rounded down.  If the length is even, then take the middle element rounded down (-1), and then one more, and find the average of the two.  Otherwise, if it's odd just take the middle element rounded down.

    def findMedianSortedArray(self, nums):
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2 - 1] + nums[length // 2]) / 2
        else:
            return nums[length // 2]

# Time: O(1)
# Space: O(1)
            k += 1
            i += 1
            else:
                mergedArrays[k] = nums2[j]
                k += 1
                j += 1

        # Store remaining elements of first array
        while i < n1:
            mergedArrays[k] = nums1[i]
            k += 1
            i += 1

        # Store remaining elements of second array
        while j < n2:
            mergedArrays[k] = nums2[j]
            k += 1
            j += 1

        return mergedArrays

# Time: O(N1 + N2)
# Space: O(N1 + N2)

# to find the median, calculate the length, and then find the element at the middle, rounded down.  If the length is even, then take the middle element rounded down (-1), and then one more, and find the average of the two.  Otherwise, if it's odd just take the middle element rounded down.

    def findMedianSortedArray(self, nums):
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2 - 1] + nums[length // 2]) / 2
        else:
            return nums[length // 2]

# Time: O(1)
# Space: O(1)
