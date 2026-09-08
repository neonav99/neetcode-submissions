class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","/","*"]
        nums = []
        for token in tokens:
            if token not in operators:
                nums.append(int(token))
                print(token)
            else:
                int_b = nums.pop()
                int_a = nums.pop()
                if token == "+":
                    val = int_a+int_b
                    nums.append(val)
                elif token == "*":
                    val = int_a*int_b
                    nums.append(val)
                elif token == "/":
                    if int_a * int_b >= 0:
                        val = int(int_a / int_b)  # Truncate towards zero for same sign division
                    else:
                        val = -(-int_a // int_b)  # Handle opposite sign division
                    nums.append(val)
                elif token == "-":
                    val = int_a-int_b
                    nums.append(val)
        if len(nums) == 0:
            return None
        else:
            return int(nums[0])
            
            

        