def solution(s):
    new=[]
    if (len(s)%2 == 0):
        n=int(len(s)/2)
        for x in range (0,len(s),2):
            new.append(s[x]+s[x+1])
        return(new)
    else:
        n=int(len(s)/2)
        for x in range (0,len(s)-1,2):
            new.append(s[x]+s[x+1])
        new.append(s[len(s)-1]+'_')
        return(new)
    pass
