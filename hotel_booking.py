'''
Problem Description:
A hotel manager has to process N advance bookings of rooms for the next season. His hotel has C rooms. Bookings contain an arrival date and a departure date. He wants to find out whether there are enough rooms in the hotel to satisfy the demand. Write a program that solves this problem in time O(N log N) .

Input Format"
First argument is an integer array A containing arrival time of booking.
Second argument is an integer array B containing departure time of booking.
Third argument is an integer C denoting the count of rooms.

Output Format:
Return True if there are enough rooms for N bookings else return False.
Return 0/1 for C programs.

Example Input:
Input 1:
 A = [1, 3, 5]
 B = [2, 6, 8]
 C = 1

Example Output:
Output 1:
 0

Example Explanation:
Explanation 1:
 At day = 5, there are 2 guests in the hotel. But I have only one room.
'''
def hotel(arrive, depart, K):
        arrive.sort()
        depart.sort()
        print(arrive,"\n",depart)
        for i in range(len(arrive)):
            if i+K<len(arrive) and arrive[i+K]<depart[i]:
                return False
        return True

if __name__=="__main__":
    A=[ 13, 14, 36, 19, 44, 1, 45, 4, 48, 23, 32, 16, 37, 44, 47, 28, 8, 47, 4, 31, 25, 48, 49, 12, 7, 8 ]
    B=[ 28, 27, 61, 34, 73, 18, 50, 5, 86, 28, 34, 32, 75, 45, 68, 65, 35, 91, 13, 76, 60, 90, 67, 22, 51, 53 ]
    C=23
    #A = [1, 3, 5]
    #B = [2, 6, 8]
    #C = 2
    result=hotel(A,B,C)
    print(result)
