'''
|Problem Description:|

Given an integer array A of size N.
You can pick B elements from either left or right end of the array A to get maximum sum.
Find and return this maximum possible sum.
NOTE: Suppose B = 4 and array A contains 10 elements then:
You can pick first four elements or can pick last four elements or can pick 1 from front and 3 from back etc . you need to return the maximum possible sum of elements you can pick.

|Input Format:|

First argument is an integer array A.
Second argument is an integer B.

|Output Format:|

Return an integer denoting the maximum possible sum of elements you picked.

|Example Input:|
A = [5, -2, 3 , 1, 2]
B = 3

|Example Output:|
8
'''

def solve_approch1(A, B):
        asum=0
        max=sum(A[0:B])
        for i in range(1,B+1):
            psum=0
            ssum=0
            if(i==B):
                asum=sum(A[(len(A)-B):])
            else:
                for j in range(0,i):
                    psum+=A[j]
                for k in range((len(A)-(B-i)),len(A)):
                    ssum+=A[k]
                asum=psum+ssum
            if(asum>max):
                max=asum
        return max

def solve_approch2(A, B):
        t=sum(A[:B])
        b=t
        for i in range(1,B+1):
            t=t-A[B-i]+A[len(A)-i]
            if b<t:
                b=t
        return b

if __name__=="__main__":

    A=[-712, -894, 40, -58, 264, -352, 446, 805, 890, -271, -630, 350, 6, 101, -607, 548, 629, -377, -916, 954, -244, 840, -34, 376, 931, -692, -56, -561, -374, 323, 537, 538, -882, -918, -71, -459, -167, 115, -361, 658, -296, 930, 977, -694, 673, -614, 21, -255, -76, 72, -730, 829, -223, 573, 97, -488, 986, 290, 161, -364, -645, -233]        
    B=34
    # Expected output=2462
    print("Solve Approch1: ",solve_approch1(A,B))
    print("Solve Approch2: ",solve_approch2(A,B))
