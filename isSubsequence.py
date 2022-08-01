class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s) <= len(t)):
            place1 = -1
            for i, letter in enumerate(s):
                try:
                    #print(letter)
                    place2 =  [j for j, x in enumerate(t) if x == letter] 
                    place2 = [x for j,x in enumerate(place2) if x > place1]
                    if not place2:
                        return False
                    else:
                        place1 = place2[0] 
                except:
                    return False
            return True
        return False