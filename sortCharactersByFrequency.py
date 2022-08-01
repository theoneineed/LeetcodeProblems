class Solution:
    def frequencySort(self, s: str) -> str:
        char_set = set(s)
        dict = {}
        for i in char_set:
            count = 0
            for x in s: 
                if i ==x: 
                    count+=1
            dict[i] = count
        
        char_set_sorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        output =""
        for i in range(len(char_set_sorted)):
            output = output + char_set_sorted[i][0]*char_set_sorted[i][1]
        return output