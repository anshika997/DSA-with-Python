class Solution:
    def canPlaceFlowers(self, fl, n) :
        for i in range(len(fl)):
            if i == 0:
                if len(fl) == 1:
                    if fl[i] == 0:
                        fl[i] = 1
                        n -= 1
                elif fl[i] == 0 and fl[i+1] == 0:
                    fl[i] = 1
                    n -= 1
            if i == 0 :
                if fl[i] == 0 and fl[i+1] == 0:
                        fl[i] = 1
                        n -= 1
            elif i == len(fl) - 1:
                if fl[i] == 0 and fl[i-1] == 0:
                    fl[i] = 1
                    n -= 1

            else :
                if fl[i] != 1 and fl[i-1] == 0 and fl[i+1] == 0 :
                    fl[i] = 1
                    n -= 1 

        if n>=1:

            return False 

        else :

            return True  
Solution = Solution()
print(Solution.canPlaceFlowers([1,0,0,0,1],1))