class Solution(object):
    def longestPalindrome(self, s):
        def ispalindrome(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left+1: right]
            
            

        ans = ""
        for i in range(len(s)):
            p1 = ispalindrome(i,i+1)
            p2 = ispalindrome(i,i)

            if len(p1) > len(ans):
                ans = p1

            if len(p2) > len(ans):
                ans = p2

        return ans

        """
        :type s: str
        :rtype: str
        """
        