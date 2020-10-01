'''
Problem Description:
Given an array of integers, sort the array into a wave like array and return it,
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example:

Given [1, 2, 3, 4]
One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]

NOTE : If there are multiple answers possible, return the one thats lexicographically smallest.
So, in example case, you will return [2, 1, 4, 3]
'''

def wave(A):
        A.sort()
        B=[]
        n=len(A)
        if n%2==0:
            for i in range(0,n,2):
                B.append(A[i+1])
                B.append(A[i])
            return B 
        else:
            for i in range(0,n-1,2):
                B.append(A[i+1])
                B.append(A[i])
            B.append(A[n-1])
            return B

if __name__=="__main__":
    print("Enter the elements in the array: ")
    A=list(map(int,input().split(" ")))
    B=wave(A)
    print(B)