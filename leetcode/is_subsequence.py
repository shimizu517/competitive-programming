# From: https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        si = 0
        s_size = len(s)
        for _t in t:
            if s[si] == _t:
                si += 1
            # All chars in s were found in t.
            if si == s_size:
                return True

        return False
