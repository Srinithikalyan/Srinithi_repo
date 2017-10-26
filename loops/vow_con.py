#A program to print vowels and consonant letters from a user's input

print "***********Vowels and consonants**********"


str = str(raw_input("\n Enter the string to find vowels and consonants "))
vow = "aeiou"


for iter in str:
    if iter in vow:
        print "\n\"%s\" is Vowel in the word \"%s\"\n " % (iter,str)
    else:
        print "\n\"%s\" is Consonant in the word \"%s\"\n " % (iter,str)

