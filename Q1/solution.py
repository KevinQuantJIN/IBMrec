def checkTshirt(n,ls,k,lk):
    hashTable = dict([('xs',0),('XS',0),('S',0),('M',0),('L',0),('XL',0),('xl',0)])
    for i in range(n):
        if len(ls[i])==1 or ls[i][1] != 'X':
            hashTable[ls[i]] = 1
        elif ls[i][-1] == 'L':
            hashTable['xl'] = 1
        elif ls[i][-1] == 'S':
            hashTable['xs'] = 1
    print(hashTable)
    flag = 0
    for i in range(k):
        if len(lk[i])==1 or lk[i][1] != 'X':
            if checkSatisfy(lk[i],hashTable):
                flag += 1
        elif lk[i][-1] == 'L':
            if hashTable['xl'] == 1:
                flag += 1
        elif lk[i][-1] == 'S':
            if checkSatisfy('xs',hashTable):
                flag += 1
    if flag == k:
        return 'Yes'
    else:
        return 'No'
def checkSatisfy(chr,table):
    seq = ['xs','XS','S','M','L','XL','xl']
    i = seq.index(chr)
    for d in seq[i:]:
        if table[d] == 1:
            return True
    return False
import sys
if __name__ == '__main__':
    length = int(sys.stdin.readline().strip())
    ls = sys.stdin.readline().strip().split()
    k = int(sys.stdin.readline().strip())
    lk = sys.stdin.readline().strip().split()
    sys.stdout.write(checkTshirt(length,ls,k,lk))

