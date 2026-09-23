class Solution:
    def repeatedSubstringPattern(self, s) :

        string = s

        if len(string) < 2:
            return False

        for i in range(1, len(string)):

            # substring ki length poori string ko divide karni chahiye
            if len(string) % i == 0:

                r = string[:i]

                # check karo r repeat karke original string banti hai ya nahi
                if r * (len(string) // i) == string:
                    return True

        return False
Solution = Solution()
print(Solution.repeatedSubstringPattern("abab"))