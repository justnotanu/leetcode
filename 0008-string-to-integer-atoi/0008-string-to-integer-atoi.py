class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Trim leading whitespace
        s = s.lstrip()
        
        if not s:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        index = 0
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        # Step 3: Read digits and handle leading zeros
        num = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            num = num * 10 + digit
            
            # Step 5: Handle overflow for 32-bit signed integer
            if sign == 1 and num >= (2**31 - 1):
                return 2**31 - 1
            if sign == -1 and num > (2**31):
                return -2**31
            
            index += 1
        
        # Step 6: Return the final result with sign
        return sign * num

        