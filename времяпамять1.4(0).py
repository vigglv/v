import time
import psutil
t_start = time.perf_counter()
def f(a, b):
    return a+b**2
with open('input.txt', 'r') as file:
    k= file.readline()
a,b = map(int, k.split())
if -10**9<=a<=10**9 and -10**9<=b<=10**9:
    m=f(a,b)
    with open('output1.txt', 'w') as file:
        file.write(str(m))
else:
    print('не выполняется')

print('%s сек' % (time.perf_counter() - t_start))
print((psutil.Process().memory_info().rss)/1024**2)
