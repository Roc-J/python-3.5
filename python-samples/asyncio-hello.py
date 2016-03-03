import asyncio
import threading

@asyncio.coroutine
def hello():
      print('Hello world! (%s)' % threading.current_thread())
      #异步调用asyncio.sleep(1):
      yield from asyncio.sleep(1)
      print("Hello again! (%s) " % threading.current_thread())

#获取EventLoop:
loop=asyncio.get_event_loop()
#执行coroutine
tasks=[hello(),hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
