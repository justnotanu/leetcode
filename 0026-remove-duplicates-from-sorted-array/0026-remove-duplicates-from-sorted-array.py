class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle the edge case for empty list

        k = 1  # Pointer for the position of unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Check if the current element is different from the last unique element
                nums[k] = nums[i]  # Place the unique element at the k-th position
                k += 1  # Move the pointer forward

        return k  # Return the number of unique elements
