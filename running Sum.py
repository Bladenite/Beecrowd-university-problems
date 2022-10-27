def pivotIndex(nums: list[int]):
    for i in range(len(nums)):
        leftsum = 0
        rightsum = 0
        for j in range(i - 1, -1, -1):
            leftsum = nums[j] + leftsum
        for k in range(i, len(nums) - 1):
            rightsum = nums[k+1] + rightsum
        if leftsum == rightsum:
            return i
    return -1
