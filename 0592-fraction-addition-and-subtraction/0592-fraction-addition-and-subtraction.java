class Solution {
    public String fractionAddition(String expression) {
        // extract the numbers with sign and add it to the stack the if there is an / sign pop the item and do operation and then add to the 
        //  stack and readd the result to the stack ( we dont need stack as we can p[rocess on the go])
        // keep doing the operations on stack until the stack size beome one thats when we do op, we can do the sum or addition based - or + and then use formula (a*d - b*c)/ c*d 
        int numerator = 0;
        int denominator = 1;
        int i = 0;
        int n = expression.length();
        
        while (i < n) {
            // Parse the numerator
            int sign = 1;
            if (expression.charAt(i) == '+' || expression.charAt(i) == '-') {
                if (expression.charAt(i) == '-') {
                    sign = -1;
                }
                i++;
            }
            int num = 0;
            while (i < n && Character.isDigit(expression.charAt(i))) {
                num = num * 10 + (expression.charAt(i) - '0');
                i++;
            }
            num *= sign;
            
            // Parse the denominator
            i++; // skip '/'
            int denom = 0;
            while (i < n && Character.isDigit(expression.charAt(i))) {
                denom = denom * 10 + (expression.charAt(i) - '0');
                i++;
            }
            
            // Perform the addition
            numerator = numerator * denom + num * denominator;
            denominator = denominator * denom;
            
            // Simplify the fraction
            int gcd = gcd(Math.abs(numerator), denominator);
            numerator /= gcd;
            denominator /= gcd;
        }
        
        return numerator + "/" + denominator;
    }
    
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}