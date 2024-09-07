# From: https://leetcode.com/problems/isomorphic-strings/submissions/1381219658/?source=submission-ac

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        memo_s = {}
        memo_t = {}
        for i in range(len(s)):
            if s[i] not in memo_s:
                memo_s[s[i]] = t[i]
            if t[i] not in memo_t:
                memo_t[t[i]] = s[i]

            if memo_s[s[i]] != t[i] or memo_t[t[i]] != s[i]:
                return False

        return True
