class Solution(object):
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        maxans = 0
        while i < j:
            length = min(height[i], height[j])
            width = j-i
            maxans = max(maxans, length * width)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxans


        """
        :type height: List[int]
        :rtype: int
        """
        