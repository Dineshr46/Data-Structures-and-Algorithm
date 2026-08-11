class Solution(object):
    def twoSum(self, nums, target):
        freq = defaultdict(int)
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in freq:
                return [freq[diff],i]
            freq[nums[i]] = i
        return -1

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        