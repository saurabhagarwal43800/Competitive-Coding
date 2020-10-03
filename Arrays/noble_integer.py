'''
Problem Description:
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p.

Input Format:
First and only argument is an integer array A.

Output Format:
Return 1 if any such integer p is found else return -1.

Example Input:

Input 1:
 A = [3, 2, 1, 3]

Input 2:
 A = [1, 1, 3, 3]

Example Output:

Output 1:
 1
Output 2:
 -1
'''

def solve(A):
        A.sort()
        for i in range(len(A)-1):
            if A[i]==A[i+1]:
                continue
            if A[i]==(len(A)-i-1):
                return 1
        if A[len(A)-1]==0:
            return 1
        return -1

if __name__ == "__main__":
    print("Enter elements in the array: ")
    A=list(map(int,input().split(" ")))
    result=solve(A)
    print(result)

    