class Hello(object):
      def hello(self,name='world'):
            print('Hello,%s'% name)

def application(environ,start_response):
      start_response('200 OK',[('Content-Type','text/html')])
      body='<h1>Hello,%s!</h1>'% (environ['PATH_INFO'][1:] or 'web')
      return [body.encode('utf-8')]
