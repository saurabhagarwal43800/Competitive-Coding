'''
Problem Description: 
Given a number N >= 0, find its representation in binary.

Example:

if N = 6,
binary form = 110
'''

def findDigitsInBinary(A):
        n=A
        i=0
        rev=0
        while(n>0):
            r=n%2
            rev+=pow(10,i)*r
            i+=1
            n=n//2
        return rev

if __name__ == "__main__":
    A=int(input("Enter the decimal number to convert into binary : "))
    print(findDigitsInBinary(A))