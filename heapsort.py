class Solution:
    def heap(self, nums, n, i):
        large = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and nums[left] > nums[large]:
            large = left
        if right < n and nums[right] > nums[large]:
            large = right

        if large != i:
            nums[i], nums[large] = nums[large], nums[i]
            self.heap(nums, n, large)

    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heap(nums, n, i)
        for j in range(n - 1, 0, -1):
            nums[j], nums[0] = nums[0], nums[j]
            self.heap(nums, j, 0)

        return nums
