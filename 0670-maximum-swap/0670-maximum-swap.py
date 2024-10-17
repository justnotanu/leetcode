class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits
        digits = list(str(num))
        last = {int(d): i for i, d in enumerate(digits)}  # Last occurrence of each digit
        
        # Iterate through each digit
        for i in range(len(digits)):
            current_digit = int(digits[i])
            
            # Check for a larger digit that appears later
            for d in range(9, current_digit, -1):  # Check from 9 down to current_digit + 1
                if d in last and last[d] > i:  # Found a larger digit later
                    # Swap
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int(''.join(digits))  # Return the new number after swap
        
        return num  # No swap was made, return original number
