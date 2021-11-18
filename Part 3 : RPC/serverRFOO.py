import rfoo
class MyHandler(rfoo.BaseHandler):
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


rfoo.InetServer(MyHandler).start()
