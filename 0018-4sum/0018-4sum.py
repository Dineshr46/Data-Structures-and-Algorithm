class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j+1
                l = n-1
                while k < l:
                    ans = nums[i] + nums[j] + nums[k] + nums[l]
                    if ans == target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        while k < l and nums[k] == nums[k+1]:
                            k+=1
                        while k < l and nums[l] == nums[l-1]:
                            l-=1
                        k+=1
                        l-=1
                    elif ans > target:
                        l-=1
                    else:
                        k+=1
        return res
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        