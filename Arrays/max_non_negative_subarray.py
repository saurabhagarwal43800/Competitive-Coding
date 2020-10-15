def maxset(A):
        subarr=[]
        pointer=0
        final=[]
        maxs=0
        minlen=0
        for i in range(len(A)):
            if A[i]>=0:
                continue
            else:
                subarr.append(A[pointer:i])
                pointer=i+1
        subarr.append(A[pointer:])
        mx=sum(subarr[0])
        for j in subarr:
            maxs=sum(j)
            if maxs>mx:
                mx=maxs
                final=j
            elif maxs==mx:
                if len(j)>minlen:
                    minlen=len(j)
                    final=j
        return final
    
if __name__=="__main__":
    A=[]
    print("Enter the elements in the array: ")
    A=list(map(int,input().split(" ")))
    B=maxset(A)
    print(B)