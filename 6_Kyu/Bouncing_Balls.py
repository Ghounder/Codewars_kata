def bouncing_ball(h, bounce, window):
    t=1
    if h<0 or bounce<0 or bounce >=1 or window >=h:
        return (-1)
    else:
        while(True):
            h=h*bounce
            if (h>window):
                t+=2
            else:
                break
    return(t)
