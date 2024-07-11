
def binary_search(low,high,condition):
    while low <= high:
        mid = (low+high)//2
        result = condition(mid)
        print(f"low : {low}\nhigh : {high}\nmid : {mid}\ncondition : {result}\n")
        if result == "found":
            return mid
        elif result == "left":
            high = mid-1
        elif result == "right":
            low = mid+1
    return -1

def first_position(list,num):
    def condition(mid):
        if list[mid] == num:
            if mid > 0 and list[mid-1] == num:
                return "left"
            return "found"
        elif list[mid] < num:
            return "right"
        else:
            return "left"
    
    return binary_search(0,len(list)-1,condition)

def last_position(list,num):
    def condition(mid):
        if list[mid] == num:
            if mid < len(list)-1 and list[mid+1] == num:
                return "right"
            return "found"
        elif list[mid] > num:
            return "left"
        else:
            return "right"
    
    return binary_search(0,len(list)-1,condition)

def position(list,num):
    return first_position(list,num),last_position(list,num)

print(position([0,0,1,2,3,3,3,3,3,4,5,6,10,10],3))