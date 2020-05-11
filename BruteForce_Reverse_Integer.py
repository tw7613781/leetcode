class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = str(x)
        if digits[0] != '-':
            reverse_digits = digits[::-1]
            reverse_integer = int(reverse_digits)
            if reverse_integer > pow(2,31) - 1:
                return 0
            else:
                return reverse_integer
        else:
            reverse_digits = digits[:0:-1]
            reverse_integer = int(reverse_digits)
            reverse_integer = 0 - reverse_integer
            if reverse_integer < 0 - pow(2, 31):
                return 0
            else:
                return reverse_integer

s =  Solution()
while True:
    x = input('input number: ')
    rt = s.reverse(x)
    print(rt)