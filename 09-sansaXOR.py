def sansaXor(arr):
    result = 0
    length = len(arr)
    for i in range(length):
        appearence = (i+1) * (length-i)
        if appearence%2 == 1:
            result ^= arr[i]
    return(result)

# def sansaXor(arr):
#     result = []
#     fxor = 0
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             subArr = arr[i:j+1]
#             xor = 0
#             for k in range(len(subArr)):
#                 xor = xor^subArr[k]
            
#             result.append(xor)

#     for i in range(len(result)):
#         fxor = fxor^result[i]
    
#     return(fxor)

sansaXor([50,13,2])