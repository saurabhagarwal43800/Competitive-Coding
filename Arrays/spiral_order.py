'''
Problem Description:

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.
The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:

    1. If there is a tie, then compare with segment's length and return segment which has maximum length.
    2. If there is still a tie, then return the segment with minimum starting index.

Input Format:
The first and the only argument of input contains an integer array A, of length N.

Output Format:
Return an array of integers, that is a subarray of A that satisfies the given conditions.

Input:
 A = [10, -1, 2, 3, -4, 100]

Output:
[100]

'''

def spiralOrder(A):
        T=0
        B=len(A)-1
        L=0
        R=len(A[0])-1
        dir=0
        new=[]
        while(T<=B and L<=R):
            if dir==0:
                for i in range(L,R+1):
                    new.append(A[T][i])
                T+=1
            elif dir==1:
                for i in range(T,B+1):
                    new.append(A[i][R])
                R-=1
            elif dir==2:
                for i in range(R,L-1,-1):
                    new.append(A[B][i])
                B-=1
            elif dir==3:
                for i in range(B,T-1,-1):
                    new.append(A[i][L])
                L+=1
            dir=(dir+1)%4
        return new

if __name__=="__main__":
    A=[[0,1,2,3],[4,5,6,7],[8,9,10,11]]
    B=[[1,2],[3,4],[5,6],[7,8]]
    print("Spiral Order for {} :".format(A))
    print(spiralOrder(A),"\n")
    print("Spiral Order for {} :".format(B))
    print(spiralOrder(B))