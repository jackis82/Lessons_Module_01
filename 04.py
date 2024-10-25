# a=[1,2,3,88,16,35]
# print(a)
#
# a.sort()
# print(a)
#
# a.sort(reverse=1)
# print(a)
#
# a.append(114)
# print(a)
#
# b=a.copy();
# print('b=',b)

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(matrix)
print('\n matrix=')
for row in matrix:
    print(row)

from copy import deepcopy

new_matrix=deepcopy(matrix)
print('\n new_matrix=')
for row in new_matrix:
    print(row)

matrix[1][1]='A'

def foo(a):
    for row in a:
        print(row)

print('\n matrix=')
foo(matrix)

print('\n new_matrix=')
foo(new_matrix)
# for row in new_matrix:
#     print(row)
