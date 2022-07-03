# Teaching math by using python
## Fibonacci
Fibonacci is an integer sequence usually beginning with 0 and 1. Its name comes from italian Leonardo de Pisa also known as Fibonacci. He described the growth of rabbits population by using this sequence. This sequence is known since around 1202.

```
f(n) = f(n-1) + f(n-2)
```

The program fibonacci.py returns the n first numbers of fibonacci sequence:
```
python .\fibonacci.py 7
```
## Permutation
Permutation refers to the rearrangement of its elements no matter the order of its elements.

The program permutation returns the permutation of the array passed as argument:
```
python .\permutation.py 1 2 3 4
```

## Arithmetic Progression
Arithmetic progression is a sequence of numbers whose the difference between the terms is a constant value usually called as root.

### Find a term of sequence

Given the first term as a1 and a common difference (root) as r, how could we figure out the n term:

```
f(n) = a1 + (n - 1) * r
```

argv[1] = First Term
argv[2] = Common difference (root of arithmetic progression)
argv[3] = Term we would like to find

```
python .\arithmetic-progression\findSequence.py 2 3 3
```

### Palindromic Triangle
Generates a palindromic triangle which shows number as they were a mirror o the first figures based on power of 11.
