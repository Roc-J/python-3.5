def count():
      fs=[]
      for i in range(1,4):
            def f():
                  return i*i
            fs.append(f)
      return fs


def count1():
      def f(j):
            def g():
                  return j*j
            return g
      fs=[]
      for i in range(1,4):
            fs.append(f(i))
      return fs

import functools
def log(func):
      @functools.wraps(func)
      def wrapper(*args,**kw):
            print('call %s():' %func.__name__)
            return func(*args,**kw)
      return wrapper
@log
def now():
      print('2016-2-18')

import functools
def log(text):
      def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                  print('%s %s():' % (text,func.__name__))
                  return func(*args,**kw)
            return wrapper
      return decorator
@log('execute')
def now():
      print('2016-2-19')



import functools
def test(text=''):
      def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                  print('end:')
                  return func(*args,**kw)
            print('begin')
            return wrapper
      return decorator
@test()
def now():
      pass
