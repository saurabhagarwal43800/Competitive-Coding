import math
def allFactors(A):
        B=[]
        for i in range(1,int(math.sqrt(A))+1):
            if A%i==0:
                B.append(i)
                if A/i!=i:
                    B.append(A//i)
        B.sort()
        return B

if __name__ == "__main__":
    A=int(input("Enter a number to find all factors upto that number: "))
    print(allFactors(A))
