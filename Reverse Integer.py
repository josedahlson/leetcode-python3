class Solution:
    def reverse(self, x: int) -> int:
        reverse_int = str(abs(x))
        reverse_int = int(reverse_int[::-1])

        if reverse_int > 2**31 - 1 or reverse_int < -2**31:
            return 0
        else:
            return reverse_int if x > 0 else -reverse_int 
