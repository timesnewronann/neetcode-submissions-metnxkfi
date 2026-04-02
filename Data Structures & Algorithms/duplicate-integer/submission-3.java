class Solution {
    public boolean hasDuplicate(int[] nums) {
        // we can solve this with a hashSet
        // we add all the items into a set
        HashSet<Integer> numberSet = new HashSet<>();

        // go through the list of numbers
        for (int i = 0; i < nums.length; i++) {
            // check if the current number is in the hashSet
            if (numberSet.contains(nums[i])) {
                return true;
            }
            // add the number into the set
            numberSet.add(nums[i]);
        }

        return false;
    }
}
