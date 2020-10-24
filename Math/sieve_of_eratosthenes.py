'''
Problem Description:
Given a number N, find all prime numbers upto N ( N included ).

Example:

if N = 7, all primes till 7 = {2, 3, 5, 7}
Make sure the returned array is sorted.
'''
#Sieve of Eratosthenes to find all prime numbers upto n
def sieve(A):
        Prime=[1]*(A+1)
        Prime[0]=0
        Prime[1]=0
        for i in range(2,int(A**0.5)+1):
            if Prime[i]==1:
                j=2
                while(i*j<=A):
                    Prime[i*j]=0
                    j+=1
        P=[i for i in range(len(Prime)) if Prime[i]==1]
        return P
if __name__ == "__main__":
    A=int(input("Enter the number to find all prime number upto : "))
    print(sieve(A))