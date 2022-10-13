# a = [1, 2, 3, 4]
# b = [4, 5, 6, 7]
import sys

if __name__ == '__main__':
    # sys.stdin = open('prob3.in', 'r') #input from file
    a = [int(x) for x in input().split()] #input for the array A
    b = [int(x) for x in input().split()] #input for the array B

    a+=b
    a.sort()

    print(a)
