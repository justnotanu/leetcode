class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string in the array
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]

        return shortest       