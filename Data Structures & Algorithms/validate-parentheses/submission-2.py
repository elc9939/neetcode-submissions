class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        arr = ['()','[]','{}']
        for i in range(len(s)):
            for j in range(3):
                if s[i] == arr[j][0]:
                    stack.append(s[i])
                elif s[i] == arr[j][1]:
                    if len(stack) == 0:
                        return False
                    p = stack.pop()
                    if p != arr[j][0]:
                        return False
        return len(stack) == 0