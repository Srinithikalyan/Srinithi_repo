print "***Replacing character on odd position with X on string***"
string = raw_input("\nEnter the string: ")
for i in range(len(string)): 
    if i % 2 == 1:
        string_1 = string.replace(string[i],'X')
    i+=2
print(string_1)
    

