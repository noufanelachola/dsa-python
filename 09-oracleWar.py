def nextQuestion(N,majority_exists,lies,num_colors,lie_number,D,queries):
    query_results = [[-1]*N for _ in range(N)]

    for query in queries:
        A,B,result = query

        if result == "YES" :
            query_results[A][B] = 1
            query_results[B][A] = 1
        else :
            query_results[A][B] = 0
            query_results[B][A] = 0

    count = [0]*N
    for i in range(N):
        for j in range(N):
            if query_results[i][j] == 1:
                count[1] += 1
                count[j] += 1

    if len(queries) >= N // 2:
        majority_ball = count.index(max(count))
        return majority_ball

    for i in range(N):
        for j in range(i + 1, N):
            if query_results[i][j] == -1:
                return (i, j)
