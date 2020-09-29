def rotateArray(a, b):
    ret = 0
    for i in range(b):
        ret=a.pop(0)
        a.append(ret)
    return a

if __name__=="__main__":
    a=[1,2,3,4,5,6,7,8]
    b=4
    print(rotateArray(a,b))