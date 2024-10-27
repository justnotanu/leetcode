class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer for the position of the next valid element

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move valid element to the front
                k += 1  # Increment the count of valid elements

        return k  # Return the count of valid elements

