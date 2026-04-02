class Solution {
    public int[] twoSum(int[] nums, int target) {
        // use a hashMap
        HashMap <Integer, Integer> prevMap = new HashMap<>();

        // go through the array
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            // we want the index and number
            int diff = target - num;

            // check if the diff is in the hashMap
            if (prevMap.containsKey(diff)){
                return new int[] {
                    prevMap.get(diff), i};
                }
                prevMap.put(num,i);
            }


            return new int [] {};
        }
    }
