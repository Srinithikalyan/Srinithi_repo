print "*******break and continue******"

while True:
    char = str(raw_input("\n Enter the key \'n\' to break the loop and \'y\' to continue "))
    if char == 'n':
        break
    elif char == 'y':
        continue
    else:
        print("\n Please choose correct option")

