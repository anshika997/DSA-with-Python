class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"

        for _ in range(n - 1):
            new_str = ""
            count = 1

            for i in range(1, len(res)):
                if res[i] == res[i - 1]:
                    count += 1
                else:
                    new_str += str(count) + res[i - 1]
                    count = 1

            # last group handle
            new_str += str(count) + res[-1]

            res = new_str

        return res
object = Solution()
print(object.countAndSay(4)) # 1211