from collections import defaultdict 

class Solution:
    def anagram(self, strs:list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()        

sl = Solution()
ls = ["eat","tea","tan","ate","nat","bat"]
print(sl.anagram(ls))


