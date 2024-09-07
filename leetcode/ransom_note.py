# From: https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_hash = defaultdict(int)
        for m in magazine:
            magazine_hash[m] += 1

        for r in ransomNote:
            if r not in magazine_hash:
                return False
            if magazine_hash[r] == 0:
                return False
            magazine_hash[r] -= 1

        return True
