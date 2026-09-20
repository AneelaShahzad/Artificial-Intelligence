def insertion_sort(li):
    for x in range(1,len(li)):
        key=li[x]
        i=x-1
        while i>-1 and li[i]>key:
            li[i+1]=li[i]
            i=i-1
        li[i+1]=key

num=[2,10,7,8,9,5,11,12]
print("Unsorted :",num)
insertion_sort(num)
print("sorted :",num)
