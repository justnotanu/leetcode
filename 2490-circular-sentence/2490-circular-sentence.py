class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Split the sentence into words
        words = sentence.split()
        
        # Check circular conditions
        n = len(words)
        
        for i in range(n):
            # Compare last character of current word with first character of next word
            if words[i][-1] != words[(i + 1) % n][0]:
                return False
        
        return True
        