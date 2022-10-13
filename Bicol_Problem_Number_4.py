# b_ = dict()
# b_.__setitem__('color',{})
# b_.get('color').__setitem__('blue', {})
import sys

if __name__ == '__main__':
    sys.stdin = open('prob4.in', 'r')
    todo_infinite = dict()
    iterc = todo_infinite.__iter__
    iterc.
    pre_set = dict()
    while True:
        try:
            
            todo = input().split() # input format : command - {goto, set, set-top}: value example goto colors
            if todo[0] == 'set-top':
                pre_set = todo_infinite
            elif todo[0] == 'set':
                pre_set.__setitem__(todo[1], {})
            elif todo[0] == 'goto':
                pre_set = pre_set[todo[1]]
        except EOFError: break

    mem

print(b_)