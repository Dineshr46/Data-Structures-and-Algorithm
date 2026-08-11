class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = 0
        mindiff = float('inf')
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                diff = abs(target - res)
                if diff < mindiff:
                    mindiff = diff
                    ans = res
                if res > target:
                    k-=1
                elif res < target:
                    j+=1
                else:
                    return res
        return ans
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        