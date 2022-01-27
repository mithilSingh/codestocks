from random import randint
from time import time
a=[randint(0,100) for i in range(10)]

def bubble_sort(l):
    for i in range(len(l)):
        for i in range(len(l)):
            try:
                x,y=l[i],l[i+1]
                if x>y:
                    l[i],l[i+1]=y,x
            except IndexError:
                pass
    return l

def selection_sort(l):

    for i in range(len(l)):
        a=(max(l)+1,None)
        for j in range(i,len(l)):
            if l[j]<a[0]:
                a=l[j],j
        l.pop(a[1])
        l.insert(i,a[0])
    return l

def insertion_sort(l):
    for i in range(1,len(l)):
        k=l[i-1]
        b=1
        while l[i-b+1]<k and i-b>=0:
            l[i-b+1],l[i-b]=l[i-b],l[i-b+1]
            b+=1
            k=l[i-b]

        return l
        
def count_sort(l) :
    ma=max(l)
    mi=min(l)
    count={}
    for i in range(mi,ma+1):
        count[i]=0
    for i in l:
        count[i]+=1
    for i in range(mi+1,ma+1):
        count[i]+=count[i-1]
    ol=["-"]*len(l)
    for i in l:
        ol[count[i]-1]=i
        count[i]-=1
    return ol


        


# i=time()
# insertion_sort(a)
# print(time()-i)
# # i=time()
# # bubble_sort(a)
# # print(time()-i)
# i=time()
# count_sort(a)
# print(time()-i)
# i=time()
# a.sort()
# print(time()-i)

# # print(selection_sort(a)==bubble_sort(a))

print(bytes(2))
