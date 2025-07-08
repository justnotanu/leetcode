class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:  # If the input is empty, return an empty list
            return []
        
        # Mapping from digits to letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        results = []  # List to store the combinations
        
        def backtrack(index: int, current_combination: str):
            if index == len(digits):  # If the current combination is complete
                results.append(current_combination)  # Add to results
                return
            
            current_digit = digits[index]  # Get the current digit
            letters = digit_to_letters[current_digit]  # Get corresponding letters
            
            for letter in letters:  # Iterate through the letters
                backtrack(index + 1, current_combination + letter)  # Recur with the next index
        
        backtrack(0, "")  # Start backtracking from index 0 with an empty combination
        return results  # Return the list of combinations
