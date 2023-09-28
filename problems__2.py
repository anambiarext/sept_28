#P1
def gensquares(N):
  for i in range(N):
    yield i**2
for  x in gensquares(10):
  print(x)

#P2
import random

def rand_num(low, high,n):
  for i in range(n):
    yield random.randint(low,high)
for num in rand_num(1,10,12):
  print(num)

#P3
s = 'hello'
print(list(iter(s)))
print(next(iter(s)))

#P4
import random

def normal(x):
  for i in range(10):
    return x*random.randint(1,10)

def abnormal(x):
  for i in range(10):
    yield x*random.randint(1,10)
    
    
print(normal(10))
print(list(abnormal(10)))
