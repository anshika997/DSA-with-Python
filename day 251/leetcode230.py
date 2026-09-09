class Solution:
    def destCity(self, paths):

        freq = {}

        for i in range(len(paths)):
            for j in range(len(paths[i])):
                if paths[i][j] not in freq:
                    freq[paths[i][j]] = 1
                else:
                    freq[paths[i][j]] += 1

        for city in freq:
            if freq[city] == 1:
                is_source = False

                for path in paths:
                    if city == path[0]:
                        is_source = True
                        break

                if not is_source:
                    return city
Solution = Solution()
print(Solution.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))