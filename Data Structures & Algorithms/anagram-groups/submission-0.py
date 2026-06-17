class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lst = []
        sortedlst = []
        for elem in strs:
            e = sorted(elem)
            if e not in sortedlst:
                lst.append([elem])
                sortedlst.append(e)
            else:
                for i in range(len(sortedlst)):
                    if e == sortedlst[i]:
                        lst[i].append(elem)
        return lst

