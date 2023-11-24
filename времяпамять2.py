import time
import psutil
t_start = time.perf_counter()
def f():
    with open('input2.txt', 'r') as file:
        n = int(file.read())
        if 0<=n<=45:
            fi = [0, 1]
            for i in range(2, n + 1):
                fi.append((fi[-1] + fi[-2]))
            with open('output2.txt', 'w') as file:
                file.write(str(fi[n]))
        else:
            with open('output2.txt', 'w') as file:
                file.write(str([]))
f()

print('%s сек' % (time.perf_counter() - t_start))
print((psutil.Process().memory_info().rss)/1024**2)

