'''
Problem Description:

Given a non-negative number represented as an array of digits,
add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]
the returned vector should be [1, 2, 4]
as 123 + 1 = 124.
'''

def plusOne(A):
        n=len(A)
        A[n-1]+=1
        carry=A[n-1]/10
        A[n-1]=A[n-1]%10
        
        for i in range(n-2,-1,-1):
            if(carry==1):
                A[i]+=1
                carry=A[i]/10
                A[i]=A[i]%10
        if(carry==1):
            A.insert(0,1)
        for i in range(len(A)):
            if A[i]==0:
                continue
            else:
                note=i
                break
        return A[note:]

if __name__ == "__main__":
    A=[9, 9, 9, 9]
    print(A,end="")
    print(" => ", plusOne(A))
    
    B=[0, 2, 9, 9]
    print(B,end="")
    print(" => ",plusOne(B))

    C=[1, 2, 3, 8]
    print(C,end="")
    print(" => ",plusOne(C))