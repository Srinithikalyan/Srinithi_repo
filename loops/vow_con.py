# A program to print vowels and consonant letters from a user's input

print "***********Vowels and consonants**********"


string = str(raw_input("\n Enter the string to find vowels and consonants "))
vow = "aeiou"


for itr in string:
    if itr in vow:
        print "\n\"%s\" is Vowel in the word \"%s\"\n " % (itr,string)
    else:
        print "\n\"%s\" is Consonant in the word \"%s\"\n " % (itr,string)

