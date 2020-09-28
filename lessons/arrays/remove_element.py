# not in place
def removeElement1(self, nums, val):
    res, count = [], 0
    for item in nums:
        if item != val:
            res.append(item)
            count += 1
    nums[:] = res
    return count

# not in place


def removeElement2(self, nums, val):
    nums[:] = [item for item in nums if item != val]
    return len(nums)

# in place


def removeElement(self, nums, val):
    l, r, count = 0, len(nums) - 1, len(nums)
    while l <= r:
        while l <= r and nums[l] == val:
            l += 1
        while l <= r and nums[r] != val:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
    for _ in xrange(l):
        del nums[0]
    return count - l


def removeElement(self, nums, val):
    l = len(nums) - 1
    for i in xrange(l + 1):
        if nums[i] == val:
            while l < i and nums[l] == val:
                l -= 1
            if l == i:
                return l
            nums[i], nums[l] = nums[l], nums[i]
    return l + 1


def removeElement(self, nums, val):
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] == val:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1
    return l
