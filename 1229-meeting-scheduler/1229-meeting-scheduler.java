class Solution {
    public List<Integer> minAvailableDuration(int[][] slots1, int[][] slots2, int duration) {
        Arrays.sort(slots1, (a,b) -> a[0] - b[0] == 0? a[1] - b[1] : a[0] - b[0]);
        Arrays.sort(slots2, (a,b) -> a[0] - b[0] == 0? a[1] - b[1] : a[0] - b[0]);

        int i = 0;
        int j = 0;
        while (i < slots1.length && j < slots2.length) {
            int sT = Math.max(slots1[i][0], slots2[j][0]);
            int eT = Math.min(slots1[i][1], slots2[j][1]);
            if(eT - sT >= duration){
                return List.of(sT, sT + duration);
            }
            else if(slots1[i][1] < slots2[j][1]){
                i++;
            }
            else{
                j++;
            }
        }
        return new ArrayList<>();
    }
}