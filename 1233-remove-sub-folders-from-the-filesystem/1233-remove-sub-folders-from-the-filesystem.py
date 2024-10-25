class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Sort the list of folder paths to ensure that parent directories are before their subfolders
        folder.sort()
        
        # Initialize the result list with the first folder since it is guaranteed not to be a subfolder
        result = [folder[0]]
        
        # Iterate through the sorted folders starting from the second folder
        for f in folder[1:]:
            # Check if the current folder is not a subfolder of the last added folder
            if not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result        