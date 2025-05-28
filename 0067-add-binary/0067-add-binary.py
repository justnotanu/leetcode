class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []  # To store the result
        carry = 0    # To keep track of carry
        i, j = len(a) - 1, len(b) - 1  # Pointers for a and b
        
        # Loop until both strings are processed and there's no carry left
        while i >= 0 or j >= 0 or carry:
            # Get the current bits (0 or 1) from each string
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            # Calculate sum of bits and carry
            total = bit_a + bit_b + carry
            
            # Update carry for next iteration
            carry = total // 2
            
            # Append the result (total % 2 gives us the current bit)
            result.append(str(total % 2))
            
            # Move to the next bits
            i -= 1
            j -= 1
        
        # The result is in reverse order, so reverse it before returning
        return ''.join(result[::-1])

   