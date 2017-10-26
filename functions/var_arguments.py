#An Example code for understanding *args and **kwargs
#Printing of multiplication table and addition of two numbers


print "*******Variable arguments *args and **kwargs *******"


def multiply(*args):        #args function definition
    for i in args:
        print "%i x 12 = %i" % (i,(i*12))


def sum(a,b):               #kwargs function definition
    sum = 0
    sum = a + b
    print "%i + %i = %i" % (a,b,sum)


print "\nThe multiplication table of 12 is"
multiply(*range(1,101))     #args function call


print "\n\nThe Addition result is"
kwargs = {'a':7,'b':3}      
sum(**kwargs)               #kwargs function call

