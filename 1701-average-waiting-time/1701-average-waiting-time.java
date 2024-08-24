class Solution {
    public double averageWaitingTime(int[][] customers) {
        // Now just calculate the total time taken for each 
        double res = 0;
        int mxTime = 0;
        for(int[] td: customers){
            res += td[1];
            if(mxTime > td[0]){
                res += (mxTime - td[0]);
                mxTime += td[1];
            }
            else{
                mxTime = td[0] + td[1];
            }
            
        }

        return res / customers.length;
    }
}