def computeEditdistance(s,t):
    cache ={}
    def recurse(m,n):
        """
        return the minimum edit distance between:
        - first m letter of s
        - first n letter of t
        """
        if (m,n) in cache:
            return cache[(m,n)]
        if m == 0:
            result = n
        elif n == 0:
            result = m
        elif s[m-1] == t[n-1]:
            result = recurse(m-1,n-1)
        else:
            subcost = 1+recurse(m-1,n-1)
            delcost = 1+recurse(m-1,n)
            inscost = 1+recurse(m,n-1)
            result= min(inscost,delcost,subcost)
        cache[(m,n)] = result
        return result
    return recurse(len(s),len(t))

print(computeEditdistance('a cat!'*10,'the cats!'*10))
