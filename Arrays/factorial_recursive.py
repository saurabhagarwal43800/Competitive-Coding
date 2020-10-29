'''
Problem Description:
Given a number A. Find the fatorial of the number.

Input Format:
First and only argument is the integer A.

Output Format:
Return a string, the factorial of A.

'''

def solve(A):
        if A>=1:
            return A * solve(A-1)
        else:
            return 1

if __name__=="__main__":
    A=int(input("Enter the number to find the factorial: "))
    print(solve(A))