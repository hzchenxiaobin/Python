class Solution:
    def punishmentNumber(self, n: int) -> int:
        def check(s, n):
            if n == int(s):
                return True
            for i in range(1, len(s)):
                if check(s[i:], n - int(s[0:i])):
                    return True
            return False
        
        res= 0 
        for i in range(1, n+1):
            if(check(str(i*i), i)):
                res += i * i
        return res