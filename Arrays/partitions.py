'''
Problem Description:
You are given a 1D integer array B containing A integers.
Count the number of ways to split all the elements of the array into 3 contiguous parts 
so that the sum of elements in each part is the same.
Such that : sum(B[1],..B[i]) = sum(B[i+1],...B[j]) = sum(B[j+1],...B[n])

Input Format:
First argument is an integer A.
Second argument is an 1D integer array B of size A.

Output Format:
Return a single integer denoting the number of ways to split the array B into three parts with the same sum.

Example Input:
Input 1:
 A = 5
 B = [1, 2, 3, 0, 3]

Input 2:
 A = 4
 B = [0, 1, -1, 0]

Example Output
Output 1:
 2

Output 2:
 1

Example Explanation
Explanation 1:

 There are no 2 ways to make partitions -
 1. (1,2)+(3)+(0,3).
 2. (1,2)+(3,0)+(3).

Explanation 2:

 There is only 1 way to make partition -
 1. (0)+(-1,1)+(0).
'''

def solve(A, B):
        if sum(B)%3!=0:
            return 0
        else:
            temp=[0]*A
            tempSum=0
            oneThird=sum(B)/3
            for i in range(A-1, -1, -1):
                tempSum+=B[i]
                if tempSum==oneThird:
                    temp[i]=1
                    
            tempSum=0
            totalCount=0
            for i in range(0,A):
                tempSum+=B[i]
                if tempSum==oneThird:
                    for j in range(i+2,A):
                        if temp[j]==1:
                            totalCount+=1
            return totalCount

if __name__ == "__main__":
    A = 5
    B = [1, 2, 3, 0, 3]
    print(B," => ",solve(A,B))
    A = 4
    B = [0, 1, -1, 0]
    print(B," => ",solve(A,B))