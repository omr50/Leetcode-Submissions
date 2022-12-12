class Solution {
public:
    int singleNumber(vector<int>& nums) {
        // get the sum of all bits.
        // It will be O(n) time and on we will
        // keep looping over the array we got all bits
        // This should at most take 32 iterations since 
        // the maximum number has 32 1 bits.
        int total = 0;
        long long twoPow = 1;
        int curr;
        for (int s = 0; s < 32; s++)
        {
        curr = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] & (1 << s))
                curr++;
        } 
            total += (twoPow * (curr%3));
            twoPow *= 2;
        }
        return total;
    }
};