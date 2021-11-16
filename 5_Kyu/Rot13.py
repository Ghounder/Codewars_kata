def rot13(message):
    alf="abcdefghijklmnopqrstuvwxyz"
    list(message)
    m=[]
    x=""
    for i in range (0,len(message)):
        if message[i].isalpha()==True:
            if message[i].isupper()==True:
                alf=alf.upper()
            else:
                alf=alf.lower()
            c=list(alf)
            index=alf.index(message[i])
            m.append(c[index-13])
        else:
            m.append(message[i])
    for i in m:
        x+=i
    return(x)
    pass
