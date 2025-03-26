class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = [0, 0]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        sum[0] = i
                        sum[1] = j
                        return sum


sol = Solution()
result = sol.twoSum([3, 3], 6)
print(result)
