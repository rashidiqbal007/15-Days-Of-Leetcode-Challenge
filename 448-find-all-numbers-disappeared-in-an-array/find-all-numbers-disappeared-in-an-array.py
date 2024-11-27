class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        missing = []
        expected = 1

        for i in nums:
            while i > expected:
                missing.append(expected)
                expected += 1
            if i == expected:
                expected += 1

        while expected <= len(nums):
            missing.append(expected)
            expected +=1 

        return missing
