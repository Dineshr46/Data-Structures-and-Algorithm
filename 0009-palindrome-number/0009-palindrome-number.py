class Solution(object):
    def isPalindrome(self, x):
        original = x
        reverse = 0
        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10
        if reverse == original:
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """
        