class solution:
    def countDigits(self,nums:int)->int:
        temp = nums
        count =0
        while temp>0:
            lastDigit=temp%10#it will shows the last digit of the number
            if nums%lastDigit==0:
                count+=1
            temp//=10
        return count
sol = solution()
print(sol.countDigits(121))