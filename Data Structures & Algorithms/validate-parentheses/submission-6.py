class Solution:
    def isValid(self, s: str) -> bool:
        dict_bracket = {}
        dict_bracket['{'] = '}'
        dict_bracket['['] = ']'
        dict_bracket['('] = ')'
        open_stack = []
        
        if len(s) == 0:
            return False

        for bracket in s:
            if bracket in dict_bracket.keys():
                open_stack.append(bracket)
            else:
                if not open_stack:
                    return False
                opening = open_stack.pop()
                dict_val = dict_bracket[opening]
                if dict_val != bracket:
                    return False
        if len(open_stack) == 0:
            return True
        else:
            return False


