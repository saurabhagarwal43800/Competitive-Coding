'''
Problem Description:
Given a number N, verify if N is prime or not.
Return 1 if N is prime, else return 0.

Example :

Input : 7
Output : True
'''

def verify(A):
    if A<2:
        return 0
    for i in range(2,int(A**0.5)+1):
        if A%i==0:
            return 0
    return 1

if __name__ == "__main__":
    A=int(input("Enter the number to verify for prime number: "))
    print(verify(A))