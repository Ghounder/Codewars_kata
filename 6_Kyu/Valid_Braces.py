def validBraces(string):
    print(string)
    b=False
    for i in range(0,len(string)):
        if i<len(string)-1:
            if string[i] == '(':
                if string[i+1] == ')' or string[i+1] =='{' or string[i+1] =='['or string[i+1] =='(':
                    b=True
                elif string[i+1] == '}' or string[i+1] ==']':
                    b=False
                    return(b)
            elif string[i]=='{':
                if string[i+1] == '}' or string[i+1] =='(' or string[i+1] =='['or string[i+1] =='{':
                    b=True
                elif string[i+1] == ')' or string[i+1] ==']':
                    b=False
                    return(b)
            elif string[i]=='[':
                if string[i+1] == ']' or string[i+1] =='{' or string[i+1] =='('or string[i+1] =='[':
                    b=True
                elif string[i+1] == ')' or string[i+1] =='}':
                    b=False
                    return(b)
        else:
            if string[i]=='[' or string[i]=='('or string[i]=='{':
                b=False
                return(b)
        print(b)
    return(b)        
    pass
