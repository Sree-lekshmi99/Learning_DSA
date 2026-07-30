class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        int l = flowerbed.length;
        for (int i=0;i<l;i++){
            if (flowerbed[i] == 0){
                boolean empty_left = (i==0) || flowerbed[i-1] == 0;
                boolean empty_right = (i == l-1) || flowerbed[i+1] == 0;
                if (empty_left && empty_right){
                    count+=1;
                    flowerbed[i]=1;
                    if (count >=l){
                        return true;
                    }

                
                }
            }
        }


    return count>=n;    
    }
}
        // count = 0
        // for i in range(len(flowerbed)):
        //     if flowerbed[i] == 0:
        //         left_space = (i==0) or flowerbed[i-1] == 0
        //         right_space = (i == len(flowerbed)-1) or flowerbed[i+1]==0
        //         if left_space and right_space:
        //             # n-=1
        //             count+=1
        //             flowerbed[i]=1
        //             if count>=n:
        //                 return True
        // return count>=n
    