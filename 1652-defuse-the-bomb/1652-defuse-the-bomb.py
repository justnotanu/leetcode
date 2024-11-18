class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        
        if k == 0:
            return result
        
        for i in range(n):
            if k > 0:
                # Sum the next k elements
                for j in range(1, k + 1):
                    result[i] += code[(i + j) % n]
            elif k < 0:
                # Sum the previous |k| elements
                for j in range(1, -k + 1):
                    result[i] += code[(i - j) % n]
        
        return result
