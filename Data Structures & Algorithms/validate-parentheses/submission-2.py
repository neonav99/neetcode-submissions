class Solution:
    def isValid(self, s: str) -> bool:
        stack_s = []
        dict_pair = {}
        dict_pair["("] = ")"
        dict_pair["{"] = "}"
        dict_pair["["] = "]"
        for element in s:
            if element in dict_pair.keys():
                stack_s.append(element)
                print(stack_s)
            else:
                if not stack_s:
                    return False
                opening = stack_s.pop()
                dict_val = dict_pair[opening]
                if dict_val != element:
                    return False
        if len(stack_s) == 0:
            return True
        else:
            return False

        
        