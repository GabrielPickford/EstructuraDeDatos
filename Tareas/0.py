class Solution(object):
    def majorElemento(self, nums):
        """Encuentra el elemento que mas se repite en un array.
        :type nums: List[int]
        :rtype: int
        """

        m = 0
        c = 0
        for i in range(len(nums)):
            if c == 0:
                m = nums[i]
                c = 1
            else:
                if m == nums[i]:
                    c += 1
                else:
                    c -= 1
        return m


sol = Solution()
# Ejemplo de uso
result = sol.majorElemento([2, 2, 3, 2, 4, 3, 3, 3, 4, 4, 3, 4, 4, 4])
print(result)
