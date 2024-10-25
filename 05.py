import random

def func(a,b,c=30):
    print(f'{a}+{b}+{c}={a+b+c}')

func(1,2,6)
func(3,5)
func(b=3,c=5,a=8)

# / - это значит, что аргументы слева от /  должны передаваться сторго без ключей
# (positional-only argument)
def func2(a,b,/,c=30,d=40):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
func2(6,3,c=5,d=8)


# * - это значит, что аргументы спраа от * должны передаваться сторго без ключей
# (positional-only argument)
def func3(a=10,b=20,*,c=30,d=40):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
func3(a=5,c=8)

def func4(a=0,b=0,c=0,d=0):
    print(f'{a}+{b}+{c}+{d}={a+b+c+d}')
func4(3)
func4(3,10,5)
# func4(3,10,5,8,88) - будет ошибка

# делаем через args (безразмерный аргумент)
def func4(*args):
    result=0
    for item in args:
        result+=item
    print(result)
func4(3,10,5,8,88)
func4(2,8,12)
func4()

# делаем через args (безразмерный аргумент)
def func5(*args,**kwargs):
    print('\nargs: ',args)
    print('\nkwargs: ',kwargs)
    result=0
    for item in args:
        result+=item
    for item in kwargs.values():
        result-=item
    # print(result)
    return result
# возвратить кортеж:
#    return result,result,result


print(func5(3, 10, 5, 8, g=88, k=6, l=8))
# func4(2,8,12)
# func4()

# рекурсия
def rec_func(n):
    print('FUNC')
    if n>1:
        rec_func(n-1)
rec_func(5)

# для вывода суммы чисел ряда Фибоначчи
def fibo(n):
    fibo1,fibo2=0,1
    for _ in range(n):
        fibo1,fibo2=fibo2,fibo1+fibo2
    return fibo1


print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))

# для вывода суммы чисел ряда Фибоначчи
def fibo_r(n):
    if n in (0,1):
        return n;
    return fibo(n-1)+fibo(n-2)
print('\n')
print(fibo_r(0))
print(fibo_r(1))
print(fibo_r(2))
print(fibo_r(3))
print(fibo_r(4))
print(fibo_r(20))

# аннотации - не ограничение (не требуют именно указанный тип),
# просто как подсказка и для удобства вызова методов типа
def a_func(a: int,b: str) -> int:
    return (a+b)
print(a_func(3, 4))


def a_func2(a: int | str,b: int=10) -> int:
    return (a+b)
print(a_func2(3, 4))


nums=list('6184375')
lets=list('abcdefghij')
# print(nums)
random.shuffle(nums)
# print(nums)
random.shuffle(lets)
my_list=[(int(nums[i]),lets[i]) for i in range(len(nums))]
print(my_list)
print(sorted(my_list, key=lambda x: x[0]))  # сортировать по цифре
print(sorted(my_list, key=lambda x: x[1]))  # сортировать по букве

