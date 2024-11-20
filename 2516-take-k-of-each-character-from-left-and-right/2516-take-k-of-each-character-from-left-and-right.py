class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Count occurrences of each character in s
        cnt = Counter(s)
        
        # Check if it's possible to take at least k of each character
        if any(cnt[c] < k for c in "abc"):
            return -1
        
        mx = 0  # Maximum length of valid subarray
        j = 0   # Pointer for the start of the sliding window
        
        # Iterate through each character in s
        for i, c in enumerate(s):
            cnt[c] -= 1  # Decrease count for current character
            
            # Ensure we have at least k occurrences of current character
            while cnt[c] < k:
                cnt[s[j]] += 1  # Restore count for character at start pointer
                j += 1          # Move start pointer to the right
            
            # Update maximum length found
            mx = max(mx, i - j + 1)
        
        # The result is total length minus maximum valid subarray length
        return len(s) - mx
        