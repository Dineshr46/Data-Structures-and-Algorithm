class Solution(object):
    def lengthOfLongestSubstring(self, s):
        freq = defaultdict(int)
        left = 0
        right = 0
        maxlen = 0
        while right < len(s):
            ans = 0
            if s[right] in freq:
                left = max(left, freq[s[right]] + 1)
            freq[s[right]] = right
            ans = right - left + 1
            maxlen = max(maxlen, ans)
            right += 1
        return maxlen
        """
        :type s: str
        :rtype: int
        """
        