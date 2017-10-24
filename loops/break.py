print "*******break and continue******"
iter = 1
while iter != 0:
    char = str(raw_input("\n Enter the key \'n\' to break the loop and \'y\' to continue "))
    if char == 'n':
        break
    elif char == 'y':
        continue
    else:
        print("\n Please choose correct option")
iter += 1
