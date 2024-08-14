/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    
    public int firstBadVersion(int n) {
        
        // do binary search in the range of 1..n
        int low = 1;
        int high = n;

        while (low < high) {
            int mid = low + (high - low) / 2;

            boolean isBad = this.isBadVersion(mid);
            if(isBad){
                high = mid;
            }
            else{
                low = mid + 1;
            }
        }

        return low;
    }
}