from threading import Event
#创建函数对象
e = Event()
#设置set
e.set()


#qingchu 
e.clear()
print(e.is_set())

e.wait()

print('********************************')


