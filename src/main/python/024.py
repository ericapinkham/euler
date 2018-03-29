##Project Euler
##
##Problem 24
##16 August 2002
##
##A permutation is an ordered arrangement of objects.
##For example, 3124 is one possible permutation of the
##digits 1, 2, 3 and 4. If all of the permutations are
##listed numerically or alphabetically, we call it lexicographic
##order. The lexicographic permutations of 0, 1 and 2 are:
##
##012   021   102   120   201   210
##
##What is the millionth lexicographic permutation of the
##digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

## Creates a list of permutations of the digits 0-9
raw_perms=list(itertools.permutations('0123456789'))
pand_list=[]
for perm in raw_perms:
    perm_string=''
    for n in perm:
        perm_string+=n
    pand_list.append(perm_string)
print('created list of permutations')

print(pand_list[999999])
