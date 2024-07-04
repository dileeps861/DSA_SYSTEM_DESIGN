class Solution {
    public int lengthOfLIS(int[] nums) {
        TreeMap<Integer, Integer> dp = new TreeMap<>();
        int maxLength = 0;  // Variable to track the maximum length found so far

        for (int num : nums) {
            Integer maxLenKey = dp.floorKey(num - 1);
            int currentLen = (maxLenKey == null ? 0 : dp.get(maxLenKey)) + 1;

            Integer existingLen = dp.get(num);
            if (existingLen == null || existingLen < currentLen) {
                dp.put(num, currentLen);
            }

            // Update maxLength with the currentLen if it's greater
            maxLength = Math.max(maxLength, currentLen);

            // Cleanup the TreeMap to remove less useful elements
            Integer higherKey = dp.higherKey(num);
            while (higherKey != null && dp.get(higherKey) <= currentLen) {
                dp.remove(higherKey);
                higherKey = dp.higherKey(num);
            }
        }

        return maxLength;
    }
}