class Solution {
    public int[][] restoreMatrix(int[] rowSum, int[] colSum) {
        // Simple approch, for each i,j try out a number and then reduce the total number of 
        // available rowSum and colSum for that i and j. Now as this might result in 
        // not sufficeint value left so we might need to try other combination
        // So this is brutwforce appraoch and could take upto 2^n combination as to try diffenre way
        // But if we look closely and see the requiremnt, we need any one answer and we cannot have negative numer but can have 0
        // So litterally can greedly fill the row and column with biggest suitable value then rest be left with 0
        int rows = rowSum.length;
        int cols = colSum.length;
        int[][] matrix = new int[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                // Take the minimum of the current rowSum and colSum
                int minVal = Math.min(rowSum[i], colSum[j]);
                
                // Place it in the matrix
                matrix[i][j] = minVal;
                
                // Subtract this value from the rowSum and colSum
                rowSum[i] -= minVal;
                colSum[j] -= minVal;
                
            }
            
        }

        return matrix;
    }
}