import rfoo
handler = rfoo.connect(host='127.0.0.1',port=rfoo.DEFAULT_PORT)
# c = rfoo.InetConnection().connect()
# fun=rfoo.Proxy(handler)

func = rfoo.Proxy(handler)
print(func.add(2,3))


