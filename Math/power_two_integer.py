'''
Problem Description:
Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed 
as A^P where P > 1 and A > 0. A and P both should be integers.

Example:

Input : 4
Output : True  
as 2^2 = 4
'''

def isPower(A):
        if A<=1:
            return 1
        for i in range(2,int(A**0.5)+1):
            p=i
            while(p<=A):
                p=p*i
                if p==A:
                    return 1
        return 0

if __name__ == "__main__":
    A=int(input("Check the power of a number: "))
    print(isPower(A))   