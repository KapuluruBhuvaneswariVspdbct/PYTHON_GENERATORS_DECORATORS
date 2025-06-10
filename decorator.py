
#decorator without param
print("decorator without args")
print()
def fun(a):
    def wrap():
        print("hi")
        a()
        print("hello")
    return wrap
@fun
def a():
    print("bhuvaneswari")
k=a()


#decorator with params
print()
print("decorator with args")
print()
def fun1(a1):
    def wrap(b,c):
        print("hi")
        a1(b,c)
        print("hello")
    return wrap
@fun1
def a1(b,c):
    print(b+c)
m=a1(2,3)


#decorator with params
print()
print("decorator with multiple inputs args")
print()
def fun12(a12):
    def wrap(*args,**kwargs):
        print("hi")
        a12(*args,**kwargs)
        print("hello")
    return wrap
@fun12
def a12(*args,**kwargs):
    print(args)
m=a12(2,3)