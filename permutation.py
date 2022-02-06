import sys
def getPermutation(a,n):
    t = ""
    aa = a

    if n == 1:
        print (aa)
    else:
        for i in range(0,n):
            getPermutation(aa,n - 1)
            if n % 2 == 0:
                t = aa[i]
                aa[i] = aa[n-1]
                aa[n-1] = t
            else:
                t = aa[1]
                aa[1] = aa[n-1]
                aa[n-1] = t
    return aa

a = []
for z in range(1, len(sys.argv)):
    a.append(sys.argv[z])

getPermutation(a, len(a))

