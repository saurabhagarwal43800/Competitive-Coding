'''
Problem Description:
Reverse digits of an integer.

Example1:
x = 123,
return 321

Example2:
x = -123,
return -321

Return 0 if the result overflows and does not fit in a 32 bit signed integer
'''

def reverse(A):
            s=str(A)
            if A>0:
                s=int(s[::-1])
            else:
                s=int(s[0]+s[:0:-1])
            if s>=-2147483648 and s<=2147483647:
                return s
            else:
                return 0

if __name__ == "__main__":
    A=int(input("Enter any number to reverse: "))
    print(reverse(A))