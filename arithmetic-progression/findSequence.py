import sys

def findSequence(firstTerm, root, positionToDiscover):
    return firstTerm + (positionToDiscover - 1) * root

a = sys.argv
print(findSequence(int(a[1]),int(a[2]), int(a[3])))