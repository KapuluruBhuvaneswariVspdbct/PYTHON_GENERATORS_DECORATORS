def ge():
    yield 10000
    yield 99999
    yield 9999
genk=ge()
print(next(genk))
print(next(genk))
print(next(genk))


#type 2
def gen():
    for i in range(100):
        yield i
genc=gen()
for val in genc:
    print(val)
    
#type 3
def gen1():
    for i in range(100):
        yield i
gencc=gen1()
for i in range(100):
    print(next(gencc))

#generator expression 
genvc=(x for x in range(100) if x<50)
for val in genvc:
    print(val)
