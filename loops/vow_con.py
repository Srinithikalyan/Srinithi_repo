print "***********Vowels and consonants**********"
str = str(raw_input("\n Enter the string to find vowels and consonants "))
vow = "aeiou"


for i in str:
    if i in vow:
        print "\n\"%s\" is Vowel in the word \"%s\"\n " % (i,str)
    else:
        print "\n\"%s\" is Consonant in the word \"%s\"\n " % (i,str)

