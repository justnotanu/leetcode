class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0;
        
        // Calculate sum of the first k elements
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        
        int maxSum = sum;
        
        int startIndex = 0;
        int endIndex = k;
        
        // Sliding window approach to find maximum sum of k consecutive elements
        while (endIndex < nums.length) {
            sum -= nums[startIndex];   // Remove the element going out of the window
            startIndex++;
            sum += nums[endIndex];     // Add the new element coming into the window
            endIndex++;
            maxSum = Math.max(maxSum, sum);
        }
        
        // Calculate the maximum average and return it
        return (double) maxSum / k;
    }
}
