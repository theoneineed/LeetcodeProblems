class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t=""
        s_clean=""
        
        for i, letter in enumerate(s):
            if ord(letter) in range(97,123) or ord(letter) in range(48,58):
                s_clean += letter
        #print(s_clean)
        
        for i in reversed(range(len(s_clean))):
            t+=s_clean[i]
            
        #print(t)
        if t==s_clean:
            return True
        else:
            return False