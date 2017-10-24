print "***********Vowels and consonants**********"
str = str(raw_input("\n Enter the string to find vowels and consonants "))
l = len(str)
print "\n The vowels in the word \"%s\" is " % str
for i in range(l):
    if (str[i] == 'a' or 
        str[i] == 'e' or 
        str[i] == 'i' or 
        str[i] == 'o' or 
        str[i] == 'u'):
        print str[i]
print "\n The consonants in the word \"%s\" is " % str
for i in range(l):
    if (str[i] != 'a' and 
        str[i] != 'e' and 
        str[i] != 'i' and 
        str[i] != 'o' and 
        str[i] != 'u'):
        print str[i]
