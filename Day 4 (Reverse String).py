class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        #Do not return anything, modify s in-place instead.
        
        st=0
        en=len(s)-1
        while(st<=en):
            s[st],s[en]=s[en],s[st]
            st+=1
            en-=1
        """
        s.reverse()