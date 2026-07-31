class Solution {
    public boolean checkIfExist(int[] arr) {
        Set<Integer> visited = new HashSet<>();
        for (int i=0;i<arr.length;i++){
            if ( visited.contains(arr[i]*2)|| ((arr[i]%2==0) && ( visited.contains(arr[i]/2))))
                        {
                return true;
            
            }
            visited.add(arr[i]);
        }
        return false;
    }
}

