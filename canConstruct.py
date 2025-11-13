from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, needed_amount in ransom_count.items():
            available_amount = magazine_count[char]
            if available_amount < needed_amount:
                return False

        return True