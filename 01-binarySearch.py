from jovian.pythondsa import evaluate_test_case

# Test cases
tests = [
    {'input': {'cards': [15, 10, 8, 6, 5, 2, 0], 'number': 8}, 'output': 2},
    {'input': {'cards': [15, 10, 8, 6, 5, 2, 0], 'number': 15}, 'output': 0},
    {'input': {'cards': [15, 10, 8, 6, 5, 2, 0], 'number': 2}, 'output': 5},
    {'input': {'cards': [15, 10, 8, 6, 5, 2, 0], 'number': 0}, 'output': 6},
    {'input': {'cards': [2], 'number': 2}, 'output': 0},
    {'input': {'cards': [15, 10, 8, 6, 5, 0], 'number': 2}, 'output': -1},
    {'input': {'cards': [], 'number': 2}, 'output': -1},
    {'input': {'cards': [10, 10, 8, 5, 5, 5], 'number': 8}, 'output': 2},
    {'input': {'cards': [10, 10, 8, 8, 8, 5, 5, 5], 'number': 8}, 'output': 2}
]


def location(cards,number,mid):
    midCard = cards[mid]
    if midCard == number:
        if mid-1 >= 0 and cards[mid-1] == midCard:
            mid -= 1
            return location(cards,number,mid)
        else:
            return mid

    

def locateCards(cards,number):
    low = 0
    high = len(cards) - 1
    
    while low <= high:
        mid = (low+high)//2

        print(f'low : {low} , high : {high} , mid : {mid} , midNo : {cards[mid]}')
        
        if cards[mid] == number :
            return location(cards,number,mid)
        elif cards[mid] > number :
            low = mid + 1
        elif cards[mid] < number :
            high = mid - 1
    return -1

result = locateCards([10],10)
print(result)