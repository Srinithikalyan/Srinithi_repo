print "****Searching for substring*******"
string = str(raw_input("\n Enter the string "))
sub = str(raw_input("\n Enter the substring to be searched "))


if sub in string:
    print "\n The entered substring \'%s\' is present in string \'%s\'" % (sub,string)
else:
    print "\n The entered substring is not present"


print "******Reversing a string******"
print string[::-1]


print "*****Printing characters from string*****"
for iter in string:
    print iter


