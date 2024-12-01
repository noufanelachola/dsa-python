def position(list,num):
    low = 0
    high = len(list)-1

    while low <= high:

        mid = (low+high)//2

        if num == list[mid]:
            return first_position(list,num,mid),last_position(list,num,mid)
        elif num < list[mid]:
            high = mid-1
        elif num > list[mid]:
            low = mid + 1


def first_position(list,num,mid):
    while mid > 0 and list[mid-1] == num:
        mid-=1
    return mid
    
def last_position(list,num,mid):
    while mid < len(list)-1 and list[mid+1] == num:
        mid+=1
    return mid


print(position([0,0,2,5,6,8,8,8,8],8))