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
    return Prime

def primesum(A):
    Prime=sieve(A)
    for i in range(A):
        if (Prime[i] and Prime[A-i]):    # OR  [if Prime[i]==1 and Prime[A-i]==1]
            return(i,(A-i))


if __name__ == "__main__":
    A=int(input("Enter the number to find the prime sum: "))
    print(primesum(A))
