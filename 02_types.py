# a=-5
# b=abs(a)
# print(a,' И ',b)
# b=a+1
# print(b)
# f="abcdefghijk"
# print(f[1],'\t',len(f))
# print(f[-2],'\t',f[2:5],'\t',f[2:9:2])
# print(f[9:2:-1])
# print(f[::-1])
# center_f=len(f)//2
# f2=f[center_f:]+f[:center_f]
# f=f[:3]+'K'+f[5:]
# print(f)
# print(f2)
# f=f+'5'*4

f="abcdefghijk"
print(f.isdigit())
print(f.replace('c','11'))
print(f)

a='123 aBc gRGr Rr'
b=a.split()
print(a,'\t=>',b)
print(a.upper(),'\t=>',a.lower())
print(a.count('aB'))
print(a.index('Bc'))
print(a.index('Bc',3))
print(b[1])

name='John'
print(f'Имя: {name}')
a='abc'
b='a'
b+='bc'
print(id(a),'\t',id(b))

# print(help(str))

