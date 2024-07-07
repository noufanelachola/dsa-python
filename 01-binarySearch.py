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



def locateCards(cards,number):
    position = 0
    while position < len(cards):
        if cards[position] == number :
            return position
        position += 1
    return -1