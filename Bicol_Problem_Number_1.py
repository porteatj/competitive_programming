import sys
import math
if __name__ =='__main__':
    # sys.stdin = open('prob1.in', 'r') #input file

    while True:
        try:
            orig, edit = input().split()
            orig_set = set(orig)   #remove character redundancies
            orig_sl = list(orig_set)
            sum_edit = 0
            for _ in orig_sl:
                sum_edit+= edit.count(_)
            # print('original_length',len(orig))
            # print('edit_length',sum_edit)
            dist = abs(len(orig)-sum_edit)
            if [0,1].count(dist) == 1:
                print('true')
            else:
                print('false')

            # [0,1].
        except EOFError : break