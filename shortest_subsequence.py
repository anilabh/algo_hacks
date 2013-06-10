#Sample Input :
# 
#Beta gama a theta. Beta gama crack alpha alpha alpha alpha a alpha theta. oopsie Beta gama alpha theta in any language. theta alpha beta gama. oopsie Beta gama alpha theta in any language.
#________________________________________________________________________________________________________________________---------------------_______________________________________________
#
#Search Words: 'alpha', 'beta', 'gama', 'theta'
#
#Sample Output (shortest sequence highlighted by '--------'):
# 
#{'alpha': 23, 'beta': 24, 'gama': 25, 'theta': 22}
def shortestSubSeg():
    para = "Beta gama a theta. Beta gama crack alpha alpha alpha alpha a alpha theta. oopsie Beta gama alpha theta in any language. theta alpha beta gama"
    tofind = ["alpha","beta","gama","theta"]
    tofind_hash = dict()
    found_first = 0
    allfound = False
    minword = ':)'
    mindex = 0
    delta_min = 10000
    for vakl in tofind:
        tofind_hash[vakl] = -1
    
    paralist = para.split(" ")
    ii = 0
    for word in paralist:
        word = word.lower()
        word =  word.strip('.')
        if (word in tofind_hash):
            if(tofind_hash[word] == -1):
                found_first += 1
                if(found_first == len(tofind)):
                    allfound = True

            tofind_hash[word] = ii
            
            if(allfound):
                    mindex,minword = findMin(tofind_hash)
                    delta = ii - mindex
                    print(delta)
                    if(delta < delta_min):
                        delta_min = delta
                        print(tofind_hash)
        ii += 1
    return tofind_hash

#can be further optimized using a min heap
def findMin(tofind_hash):
    minc = 1000
    minkey = ''
    for key in tofind_hash:
        val = tofind_hash[key]
        if(val < minc):
            minc = val
            minkey = key
    return minc, minkey
