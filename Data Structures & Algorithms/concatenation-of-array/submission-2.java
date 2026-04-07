class Solution {
    public int[] getConcatenation(int[] nums) {
        // create a new array that is 2 times the length of nums
        int n = nums.length;
        int[] ans = new int[2*n];

        for (int i = 0; i < n; i++){
            ans[i] = ans[i +n] = nums[i];
        }

        return ans;
    }
}