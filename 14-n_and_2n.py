def checkIfExist(arr):
    elements = dict()

    for element in arr:
        if element*0.5 in elements or element*2 in elements:
            return True

        if  element not in elements:
            elements[element] = element

    return False