def find_missing_letter(chars):
    new=[]
    alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if chars[0].isupper():
        for i in range (0,len(alf)):
            alf[i]=alf[i].upper()
    index=alf.index(chars[0])
    items=len(chars)+1
    for i in range (0,items):
        new.append(alf[index+i])
    new=set(new)
    chars=set(chars)
    x=list(new.difference(chars))
    return(x[0])
