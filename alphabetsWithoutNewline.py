def alphabets(c1,c2):
    
    #Code below to print alphabets from c1 to c2
    start = ord(c1)
    stop = ord(c2)
    a=[]
    for i in range(start, stop+1):
        a.append(chr(i))
        print(chr(i), end = ' ')
    
    # Don't provide a new line after printing
