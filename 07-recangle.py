def Rectangle_Renaissance(n, a):
    maxArea = 0

    for i in range(n):
        for j in range(i,n):
            minHeight = min(a[i:j+1])
            width = j-i+1
            area = minHeight*width

            maxArea = max(maxArea,area)

    return maxArea

