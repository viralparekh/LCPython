# Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_val_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        num = 0
        pre = ""
        for c in s:
            if pre == "":
                pre = c
                num = symbol_val_dict[c]
                continue
            
            if symbol_val_dict[pre]<symbol_val_dict[c]:
                num = num - 2*symbol_val_dict[pre] + symbol_val_dict[c]
            else:
                num = num  + symbol_val_dict[c]
            pre = c
                
        return num
