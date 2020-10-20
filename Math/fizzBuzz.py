'''
Problem Description:
Given a positive integer A, return an array of strings with all the integers from 1 to N.
But for multiples of 3 the array should have “Fizz” instead of the number.
For the multiples of 5, the array should have “Buzz” instead of the number.
For numbers which are multiple of 3 and 5 both, the array should have “FizzBuzz” instead 
of the number.

Example:
A = 5
Return: [1 2 Fizz 4 Buzz]
'''

def fizzBuzz(A):
        result=[]
        for i in range(1,A+1):
            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
            elif i%3==0:
                result.append("Fizz")
            elif i%5==0:
                result.append("Buzz")
            else:
                result.append(i)
        return result

if __name__=="__main__":
    A=int(input("Enter any number for FizzBuzz: "))
    print(fizzBuzz(A))