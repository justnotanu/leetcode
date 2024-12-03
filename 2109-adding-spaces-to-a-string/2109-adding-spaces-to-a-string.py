class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        last_index = 0
        
        for space_index in spaces:
            # Append characters from last_index to space_index
            result.append(s[last_index:space_index])
            # Add a space
            result.append(' ')
            # Update last_index to current space_index
            last_index = space_index
        
        # Append any remaining characters after the last space index
        result.append(s[last_index:])
        
        # Join the list into a single string and return
        return ''.join(result)
