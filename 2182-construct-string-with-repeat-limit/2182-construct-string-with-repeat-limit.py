class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Step 1: Count occurrences of each character
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        result = []
        i = 25  # Start from 'z'
        
        while i >= 0:
            if char_count[i] == 0:
                i -= 1
                continue
            
            # Determine how many times we can add this character
            count_to_add = min(char_count[i], repeatLimit)
            result.append(chr(ord('a') + i) * count_to_add)
            char_count[i] -= count_to_add
            
            if char_count[i] > 0:  # If there are still characters left
                # Find next available character
                next_char_index = i - 1
                while next_char_index >= 0 and char_count[next_char_index] == 0:
                    next_char_index -= 1
                
                if next_char_index < 0:  # No more characters available
                    break
                
                # Add one instance of the next available character
                result.append(chr(ord('a') + next_char_index))
                char_count[next_char_index] -= 1
            
        return ''.join(result)

# Example usage:
solution = Solution()
print(solution.repeatLimitedString("cczazcc", 3))  # Output: "zzcccac"
print(solution.repeatLimitedString("aababab", 2))   # Output: "bbabaa"

        