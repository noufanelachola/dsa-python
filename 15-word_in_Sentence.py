sentence = "i love eating burger"
search = "burg"

def isPrefixOfWord(sentence,search):

    strList = sentence.split(" ")   
    
    for i,word in enumerate(strList):

        match = True

        for j in range(len(search)):
            if len(search) > len(word):
                match = False
                break
            elif word[j] != search[j]:
                match = False
                break

        if match:
            return i+1
        
    return -1

print(isPrefixOfWord(sentence,search))