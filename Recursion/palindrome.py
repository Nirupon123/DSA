class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        n = len(s)
        left=0
        right = n - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
obj = Solution()
print(obj.isPalindrome("madam"))  
print(obj.isPalindrome("hello"))   
print(obj.isPalindrome("Racecar")) 
