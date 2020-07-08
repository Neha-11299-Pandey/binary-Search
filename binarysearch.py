
def  search(array, l, u,n):
    if u>=l:

        mid_value = l+(u-1)//2
        if array[mid_value] == n:
            return mid_value
        #if element is smaller than mid_value,then it can only present in left subarray
        elif array[mid_value] > n :
            return search(array,l,mid_value-1,n)
        #Else the element can only present in the right subarray
        else:
            return search(array, mid_value+1,u,n)
    else:#Element is not present in the array
        return-1



    array = [1,3,5,7,9,11,14]
    n = 9
    result = search(array,0,l,len(array)-1,n)

    if result != -1:
        print("Element is present at index %d" %result)
    else:
        print("element is not present in array")






