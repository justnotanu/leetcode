class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        
        for num in arr:
            # Check if num is double of any number we've seen
            if num * 2 in seen:
                return True
            # Check if half of num has been seen (and num is even)
            if num % 2 == 0 and (num // 2) in seen:
                return True
            
            # Add current number to the set
            seen.add(num)
        
        return False
