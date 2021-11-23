import rfoo
class MyHandler(rfoo.BaseHandler):
    def __init__(self, handler, conn):
        self._handler = handler 
        self._conn = conn
        self._buffer = '1024'
        self._counter = 0
        self._server = rfoo.Server(self._handler)
        self._methods = {}
        self.repertoire = []

    def add(self, a,b):
        return a+b
    def mult(self,a,b):
        return a*b
    def diff(self,a,b):
        return a-b 
    def quotient(self,a,b):
        try : 
            return a/b 
        except ValueError as error :
            raise 'Division par zero {}'.format(error)
    def absolue(self,a):
        return abs(a)

rfoo.start_server(host="127.0.0.1",port=rfoo.DEFAULT_PORT,handler=MyHandler)
# rfoo.InetServer(MyHandler).start()
