# number=0
# if number==0:
#     print(f'number={number}')
# else:
#     print('false')
#
# number=50
# if number<100:
#     print('<100')
# elif number>200:
#     print('>200')
# else:
#     print('[100..200]')

# k=0
# k=input('Введите k: ')
# n=1
# while n<=int(k):
#     print(f'n={n}',end='  ')
#     if (n % 10==0):
#         print('\n')
#     n+=1

st='abcdefghijk'
# for ch in st:
#     print(ch,end='\t')
for i in range(10):
    print(st[i],end='\t')
print('')
for i in range(-1,-4,-1):
    print(st[i],end='\t')
print('')
for i in range(1,8,2):
    print(st[i],end='\t')
print('')

l=['asd','dfd','grgb']
for ch in l:
    print(ch,end='\t')
