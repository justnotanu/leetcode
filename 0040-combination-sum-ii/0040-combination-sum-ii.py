class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort the candidates to handle duplicates
        self.result = []
        
        def solve(start: int, temp: List[int], remaining: int):
            if remaining == 0:
                self.result.append(temp[:])  # Add a copy of the temp list
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:  # No need to continue if the candidate exceeds remaining
                    break
                if i > start and candidates[i] == candidates[i - 1]:  # Skip duplicates
                    continue
                
                temp.append(candidates[i])
                solve(i + 1, temp, remaining - candidates[i])
                temp.pop()
        
        solve(0, [], target)
        return self.result
                