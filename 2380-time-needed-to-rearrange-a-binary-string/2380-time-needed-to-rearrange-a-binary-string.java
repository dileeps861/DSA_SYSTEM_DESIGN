class Solution {
    public int secondsToRemoveOccurrences(String s) {
        char[] chars = s.toCharArray();
        // int second = 0;
        // while (true) {
        //     boolean falg = true;
        
        //     for(int i = 0; i < s.length()-1; i++){
        //         if(chars[i] == '0' && chars[i + 1] == '1'){
        //             char temp = chars[i];
        //             chars[i] = chars[i+1];
        //             chars[i+1] = temp;
        //             falg = false;
        //             i++;
        //         }
        //     }
        //     if(falg) return second;
        //     second++;
        // }

        // A Better approach is just have the count of preceeding zeros of a 01

        int count = 0;
        int sec = 0;
        for(int i = 0; i < chars.length; i++){
            if(chars[i] == '0') {
                count++;
            }
            else if(count > 0){
                sec = Math.max(sec+1, count);
            }
        }
        return sec;
    }
}