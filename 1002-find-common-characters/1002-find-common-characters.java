class Solution {
    public List<String> commonChars(String[] words) {
        int[] globalMinFreq = new int[26];
        // Initialize globalMinFreq with a very large value
        Arrays.fill(globalMinFreq, Integer.MAX_VALUE);

        // Update globalMinFreq with the minimum frequency of each character
        for (String word : words) {
            int[] charCount = new int[26];
            for (char c : word.toCharArray()) {
                charCount[c - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                globalMinFreq[i] = Math.min(globalMinFreq[i], charCount[i]);
            }
        }

        // Collect the result from the globalMinFreq
        List<String> res = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            while (globalMinFreq[i] > 0) {
                res.add(String.valueOf((char) (i + 'a')));
                globalMinFreq[i]--;
            }
        }

        return res;
    }
}