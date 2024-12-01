tests = [
    {
        "input" : {"list" : [1,2,3,4,5,6,7]},
        "output" : 0
    },
    {
        "input" : {"list" : [7,1,2,3,4,5,6]},
        "output" : 1
    },
    {
        "input" : {"list" : [5,6,7,1,2,3,4]},
        "output" : 3
    },
    {
        "input" : {"list" : [2,3,4,5,6,7,1]},
        "output" : 6
    },
    {
        "input" : {"list" : [1]},
        "output" : 0
    },
]

def calculateRotationLinear(list):
    i = 0
    while i < len(list)-1:
        print(f"i:{i}\n")
        if list[i] > list[i+1]:
            return i+1
        i+=1
    return 0
    
    
def calculateRotationBinary(list):
    low,high = 0,len(list)-1
    
    def condition(low,mid,high):
        if list[low] > list[mid]:
            return "left"
        elif list[mid] > list[high]:
            return "right"

    while low <= high:

        if list[low] < list[high]:
            return 0

        mid = (low+high)//2
        result = condition(low,mid,high)

        print(f"low:{low}\nmid:{mid}\nhigh:{high}\nresult:{result}\n")

        if result == "left":
            high = mid-1
        elif result == "right":
            low = mid+1
    return 0 