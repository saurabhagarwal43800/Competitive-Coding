'''
Problem Description:
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
If A is already sorted, output -1.

Example :

Input 1:
A = [1, 3, 2, 4, 5]
Return: [1, 2]

Input 2:
A = [1, 2, 3, 4, 5]
Return: [-1]
'''

def subUnsort(A):
        b=sorted(A)
        L=[]
        if b==A:
            return [-1]
        else:
            for i in range(len(A)):
                if A[i]!=b[i]:
                    L.append(i)
            return [min(L),max(L)]

if __name__ == "__main__":
    A=[1,3,2,4,5]
    B=[1,2,3,4,5]
    print(A," -> ",subUnsort(A))
    print(B," -> ",subUnsort(B))
