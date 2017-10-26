#An example program for Yield concept
#Difference between yield and return statements


print "Yield and Return statements"
def func1():
    a = 0
    while True:
        a += 1
    	return a


def func2():
    a = 0
    while True:
        a += 1
    	yield a


     
f1 = func1()
f2 = func2()


for i in range(5):
    print f1


for i in range(5):
    print next(f2)


