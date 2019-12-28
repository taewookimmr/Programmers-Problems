package kakao.binarysearch;

class Solution{
    public int solution(int[] budgets, int M){
        long sum = 0;
        for(int i = 0; i < budgets.length; i++){
            sum +=budgets[i];
        }
        if(M>=sum){
            return getMax(budgets);
        }
        
        int left = M/budgets.length;
        int right = getMax(budgets);
        int middle = 0;
        while(true){
            if (left == right || right-left == 1){
                break;
            }

            middle = (left + right) /2;
            if (func(budgets, M, middle) > 0){
                left = middle;
            }else{
                right = middle;
            }
        }
        if(func(budgets, M, left) > 0){
            return left;
        }else{
            return left-1;
        }

        
    }

    public int func(int[] budgets, int M, int limit){
        int sum = 0;
        for(int i = 0; i < budgets.length;i++){
            if(budgets[i] < limit){
                sum+= budgets[i];
            }else{
                sum+=limit;
            }
        }
        return M-sum;
    }

    public int getMax(int[] budgets){
        int max = 0;
        for(int i =0; i < budgets.length; i++){
            if(budgets[i] >= max){
                max = budgets[i];
            }
        }
        return max;
    }
    public static void main(String[] args) {
        int[] budgets ={120, 110, 140, 150};
        int M = 485;
        Solution sol = new Solution();
        int result = sol.solution(budgets, M);
        System.out.println("result = "+ result);
    }
}