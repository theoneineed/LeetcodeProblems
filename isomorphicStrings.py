class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        s_set = self.unique(s)
        t_set = self.unique(t)
        s_dict ={}
        t_dict = {}
        count = 0
        for i in range(len(s_set)):
            s_dict[i] = [index for index in range(len(s)) if s_set[i] == s[index]]

            
        for i in range(len(t_set)):
            t_dict[i] = [index for index in range(len(t)) if t_set[i] == t[index]]
        
        if len(s_dict) == len(t_dict):
            for i in range(len(s_dict)):
                if s_dict[i] != t_dict[i]:
                    return False
            return True
        return False
        
    def unique(self,sequence):
        seen = set()
        return [x for x in sequence if not (x in seen or seen.add(x))]