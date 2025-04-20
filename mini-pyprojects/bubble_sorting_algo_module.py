def arg(l):
    t=len(l)
    t2=t
    for i in range(t):
        for ti in range(1,t2):
            a=l[ti-1]
            if a>l[ti]:
                l[ti-1],l[ti]=l[ti],l[ti-1]
        t2-=1
    return(l)
