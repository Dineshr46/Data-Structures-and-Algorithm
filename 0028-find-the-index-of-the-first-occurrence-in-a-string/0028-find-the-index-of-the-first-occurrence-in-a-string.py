class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        j = len(needle)-1
        while j < len(haystack):
            if haystack[i:j+1] == needle:
                return i
            i+=1
            j+=1
        return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        