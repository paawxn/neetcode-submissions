class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count={}
        count2 = {}
        for i in s:
            if i in count:
                count[i] = count[i]+1
            else:
                count[i]=1   
        for j in t:
            if j in count2:
                count2[j]+=1
            else: count2[j]=1
        if count==count2: return True
        else: return False
