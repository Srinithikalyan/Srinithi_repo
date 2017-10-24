print "******List Operations******"
l = [1,4,3,2,6,8,34,21,56,100]
print "\nThe created list is " ; print l
ele = int(input("\nEnter the element to update list: "))
l.append(ele) ; print l
l1 = input("\nEnter the elements of new list you want to extend ")
l.extend(l1)
print "\nThe extended list is " ; print l
pos,ele1 = input("\nEnter the position and element to insert into list: ")
l.insert(pos,ele1)
print "\nList after inserting new element is " ;
print l
l.pop()
print "\nAfter pop operation, the list is " ; print l
c = 0
rem = input("\nEnter the element to remove from list ")
for i in range(len(l)):
    if l[i] == rem:
        c+=1
if c > 0:
    l.remove(rem) ; 
    print "\nThe list after removing given element" ; print l
else:
    print "\n The entered element is not in list"
print "\nThe reverse of list is "
l.reverse() ; print l
l.sort()
print "\nThe sorted list is " ; print l
occ = input("\nEnter the element to find its occurances in created list: ")
occur = l.count(occ) 
if occur > 0:
    print "\nThe element %i is occured %i times in list" % (occ,occur)
else:
    print "\nThe entered element is not in list"
ind = input("\nEnter the element to find its position in list: ")
indx = l.index(ind)
if indx < len(l):
    print "\nThe element %i is present at %i position" % (ind,indx)
else:
    print "\nThe entered element is not in list"
print "\nUsing negative slicing, the list values are displayed"
for i in range(len(l)):
    print "\nThe value at %i is %i" % (-i-1,l[-i-1])    
print "The string form of list is " ; print (str(l))
