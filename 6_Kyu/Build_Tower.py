def tower_builder(n_floors):
    t=[]
    c=""
    for i in range (0,n_floors):
        for j in range (0,(n_floors-(i+1))):
            c+=' '
        for k in range (0,(2*i+1)):
            c+='*'
        for l in range (0,(n_floors-(i+1))):
            c+=' '
        t.append(c)
        c=""
    return(t)
