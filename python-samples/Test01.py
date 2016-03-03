import math

def move(x,y,step,angle=0):
      nx=x+step*math.cos(angle)
      ny=y-step*math.sin(angle)
      return nx,ny
def power(x,n=2):
      s=1
      while n>0:
            n=n-1
            s=s*x
      return s

def fib(max):
      n,a,b=0,0,1
      while n<max:
            yield b
            a,b=b,a+b
            n=n+1
      return 'done'

def odd():
      print('step 1')
      yield 1
      print('step 2')
      yield 3
      print('step 3')
      yield 5

def add(x,y,f):
      return f(x)+f(y)

def f(x):
      return x*x

from functools import reduce

def str2int(s):
      def fn(x,y):
            return x*10+y
      def char2num(s):
            return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
      return reduce(fn,map(char2num,s))

def is_odd(n):
      return n%2==1

def not_empty(s):
      return s and s.strip()


def lazy_sum(*args):
      def sum():
            ax=0
            for n in args:
                  ax=ax+n
            return ax
      return sum

           
            
      
