class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = defaultdict(int)
        maxlen = 0
        j = 0
        i = 0
        while j < len(s):
            if s[j] in freq:
                i = max(i,freq[s[j]] + 1)
            freq[s[j]]=j
            maxlen = max(maxlen, j - i + 1)
            j+=1
        return maxlen
        """
        :type s: str
        :rtype: int
        """
        