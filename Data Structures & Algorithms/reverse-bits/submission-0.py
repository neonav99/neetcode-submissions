class Solution:
    def __init__(self):
        self.stack = [0] * 32
        self.i = 0  # next write position

    def recursive_div(self, value: int) -> None:
        # push exactly 32 "remainders" (bits)
        if self.i == 32:
            return
        self.stack[self.i] = value % 2
        self.i += 1
        self.recursive_div(value // 2)

    def reverseBits(self, n: int) -> int:
        self.i = 0                  # reset for safety if object reused
        self.recursive_div(n)        # fill stack with 32 bits (LSB -> MSB)

        # convert bits to int
        ans = 0
        for b in self.stack:
            ans = (ans << 1) | b
        return ans
