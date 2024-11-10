class Solution {
public:
    void performOrOperation(int &num, int &orVal, vector<int>& bitCount) {
        orVal = (orVal | num);
        // update bit count
        for(int i=0; i<32; i++)
            if(num & (1 << i))       // ith bit is set
                bitCount[i] += 1;
    }

    void revertOrOperation(int &num, int &orVal, vector<int>& bitCount) {
        // update bit count
        for(int i=0; i<32; i++) {
            if(num & (1 << i))       // ith bit is set
                bitCount[i] -= 1;
        
            // bitcount[i] becomes 0 --> unset ith bit
            if(bitCount[i] == 0)
                orVal = orVal & (~(1<<i));
        }
    }

    int minimumSubarrayLength(vector<int>& nums, int k) {
        int ans = INT_MAX;
        int orVal = 0;
        vector<int> bitCount(32, 0);
        // sliding window
        int l = 0;
        int r = 0;
        while(r < nums.size()) {
            // expand right boundary : include rth element
            performOrOperation(nums[r], orVal, bitCount);

            // shrink left boundary until orVal >=k
            while(l <= r && orVal >= k) {
                ans = min(ans, r - l + 1);
                revertOrOperation(nums[l], orVal, bitCount);
                l++;
            }
            r++;    // next iteration
        }
        return (ans == INT_MAX) ? -1 : ans;
    }
};