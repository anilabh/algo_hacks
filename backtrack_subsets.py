import re, urllib
import string
finished = 0 # found all solutions yet? */
MAXCANDIDATES = 1000
def is_a_solution(a,k,n):
    return (k == n)
def process_solution(a,k,input1,indent):
    print(indent+'start-------')
    print(a)
    for i in range (1,k+1):
        if(a[i]== 1):
            print(indent,i)
    print(indent+'stop=========')
    return
def construct_candidates(a,k,input1,c):
    c.append(1)
    c.append(0)
    ncandidates = 2
    return ncandidates
def make_move(a,k,input1):
    return
def unmake_move(a,k,input1):
    return
def backtrack(a, k, input1,indent):
    #print a,k,input1
    indent = indent + '*'
    c = list() # candidates for next position */
     # next position candidate count */
    i = 0 # counter */
    if (is_a_solution(a,k,input1)):
    #    print 'k = ',k
        process_solution(a,k,input1,indent)
    else:
    #    print 'else loop'
        k = k+1
        print(indent+'k = ',k)
        ncandidates = construct_candidates(a,k,input1,c)
    #    print a,k,input1,c,ncandidates
        for i in range (0,ncandidates):# (i=0; i<ncandidates; i++)
        #    print a
            a[k] = c[i]
        #    print a
            make_move(a,k,input1)
            backtrack(a,k,input1,indent)
            unmake_move(a,k,input1)
            if (finished):
                return # terminate early */

def call_backtrack_subsets():
    n = 4
    subset = 2**(n-1)
    print(subset)
    a = list()
    for i in range(0,subset):
        a.append('x')
    backtrack(a,0,n-1,'')
