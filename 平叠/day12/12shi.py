
# 1.
#在函数里边  在函数外面调用的部分
# 装饰器原理示意
#定义装饰函数   并装饰myfunc
# 装饰器的原理是替换被装饰函数的变量绑定关系
#用装饰器语法实现方法见：mydeco4.py
def mydeco(fn):
   
    def fx():
        print("++++++++++++++++++")
        
        fn()
        print("++++++++++++++++++")
    return fx
# @mydeco  
def myfunc():   
    print("myfunc被调用")
# myfunc = mydeco(myfunc)
myfunc()
myfunc()
myfunc()

########mydeco5.py

# #模拟银行的业务需求 用装饰器来扩展新业务
# ## 银行： 存钱  取钱
# #==================== 
# def privileged_check(fn):
#     def fx(n,x):
#         print("权限验证中")
#         fn(n,x)
#     return fx

# def send_message(fn):
#     #实现业务操作完成后发送短消息的功能
#     def fy(n,y):
#         fn(n,y)  #先操作 再发消息
#         print("正在发送消息给：",n,'...')
#     return fy
# @send_message
# @privileged_check
# def savemoney(name,x):
    
#     print(name,"存钱",x,'元')
   
# @privileged_check 
# def withdraw(name,x):
#     print(name,"取钱",x,"元")

# #-------------------

# savemoney('小王',200)
# savemoney('小赵',400)
# withdraw('小李',500)


# # 示例
# import time
# print("你好")
# time.sleep(2)
# print("傻蛋")



