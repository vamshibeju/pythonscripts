'''def foo(n):
    for x in range(n):
        yield x**3

for x in foo(5):
    print x,'''

def foo(value):
 while True:
     value = (yield value)

bar = foo(1)
print(next(bar))
print(next(bar))
print(bar.send(2))
