class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","/","*"]
        nums = []
        for token in tokens:
            if token not in operators:
                nums.append(token)
                print(nums)
            else:
                int_b = int(nums.pop())
                int_a = int(nums.pop())
                if token == "+":
                    val = int_a+int_b
                    nums.append(val)
                elif token == "*":
                    val = int_a*int_b
                    nums.append(val)
                elif token == "/":
                    val = int_a/int_b
                    nums.append(val)
                elif token == "-":
                    val = int_a-int_b
                    nums.append(val)
        if len(nums) == 0:
            return None
        else:
            return int(nums[0])
            

        