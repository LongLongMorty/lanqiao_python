class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        a, b = 0, 0
        a1, b1 = "", ""
        sy = True
        while a < len(s):
            if s[a] != '#':
                a1 += s[a]
                a += 1
            else:
                if a1 != "":
                    a1 = a1[:-1]
                a += 1

        while b < len(t):
            if t[b] != '#':
                b1 += t[b]
                b += 1
            else:
                if b1 != "":
                    b1 = b1[:-1]
                b += 1
        if a1 != b1:
            sy = False
        return sy
