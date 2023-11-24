import time
import psutil
t_start = time.perf_counter()
def f(a,b):
    return a+b**2
i=input('Два числа: ')
a,b=map(int, i.split())
if -10**9<=a<=10**9 and -10**9<=b<=10**9:
    r = f(a,b)
    print('Ответ: ', r)
else:
    print('Не удовлетворяет условию')

print('%s сек' % (time.perf_counter() - t_start))
print((psutil.Process().memory_info().rss)/1024**2)
