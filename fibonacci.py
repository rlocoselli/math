import sys

# position commence à zero 0
#f(n+2) = f(n+1) + f(n)
def getSuiteFibonnaci(n):
    if(n < 0):
        print("Le chiffre d'entrée doit être superieur à -1")
    else:
        i = 1
        a = 1 # chiffre preécedent
        b = 1 # chifre actuel
        print(1)
        print(1)
        
        while(i < n - 1):
            a,b = b, a+b
            i=i+1
            print(b)

getSuiteFibonnaci(int(sys.argv[1]))

