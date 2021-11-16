def duplicate_count(text):
    text=text.lower()
    f=0
    for i in text:
        print(text)
        print(i)
        c=text.count(i)
        text=text.replace(i,"")
        print(c)
        if c>1:
            f+=1
    print(f)
    return(f)
