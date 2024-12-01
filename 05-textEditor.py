def simpleTextEditor(operations):
    word = ""
    stack = []
    result = []


    for operation in operations:
        op = operation.split()

        if op[0] == 1:
            # append
            stack.append(("1",word))
            word+=op[1]
        
        elif op[0] == 2:
            #delete
            k = int(op[1])
            stack.append(("2",word))
            word = word[0:-k]
        
        elif op[0] == 3:
            #print
            k = int(op[1])
            result.append(word[k-1])
        
        elif op[0] == 4:
            #undo
            if len(stack):
                lastOp,value=stack.pop
                word = value

    for res in result:
        print(res)

                
simpleTextEditor(["1 fg","3 6","2 5","4","3 7","4","3 4"])        
