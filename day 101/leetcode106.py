# this is a greedy algorithm problem, we want to give the smallest cookie to the child with the smallest appetite, so that we can save the bigger cookies for the children with bigger appetites

# i solve this problem by iterating through the list of children and for each child, I find all the valid cookies that can satisfy their appetite, then I choose the smallest valid cookie and remove it from the original list of cookies, and increment the count of satisfied children. Finally, I return the count of satisfied children. 

# but this solution is not efficient because for each child, we are iterating through the list of cookies to find the valid cookies, which results in a time complexity of O(n*m) where n is the number of children and m is the number of cookies. 

class Solution:
    def findContentChildren(self, g, s):
        count = 0

        for i in range(len(g)):
            temp = [] 

            # find all valid cookies
            for j in range(len(s)):
                if s[j] >= g[i]:
                    temp.append(s[j])

            # if we found any valid cookie
            if temp:
                chosen = min(temp)   # smallest valid cookie
                s.remove(chosen)    # remove from original list
                count += 1

        return count
Solution=Solution()
print(Solution.findContentChildren([1,2,3], [1,1]))  # Output: 1
print(Solution.findContentChildren([1,2], [1,2,3]))