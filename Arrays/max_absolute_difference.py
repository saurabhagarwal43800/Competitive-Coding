'''
Problem Description:
You are given an array of N integers, A1, A2 ,…, AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

For example,

A=[1, 3, -1]

f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

So, we return 5.
'''

def maxArr(array):
        max1 = 0 #-2147483648
        min1 = 0 #+2147483647
        max2 = 0 #-2147483648
        min2 = 0 #+2147483647
       
        for i in range(len(array)): 
            max1 = max(max1, array[i] + i) 
            min1 = min(min1, array[i] + i) 
            max2 = max(max2, array[i] - i) 
            min2 = min(min2, array[i] - i) 

        return max(max1 - min1, max2 - min2)

if __name__ == "__main__":
    A=[1, 3, -1]
    B=[-70, -64, -6, -56, -64, -61, -57, -16, -48, -98]
    print(A," => ",maxArr(A))
    print(B," => ",maxArr(B))