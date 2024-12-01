
def timeInWords(h,m):
    time = [
            "zero","one","two","three","four","five","six","seven","eight","nine","ten",
            "eleven","tweleve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty",
            "twenty one","twenty two","twenty three","twenty four","twenty five","twenty six","twenty seven","twenty eight","twenty nine","thirty",
    ]

    hour = ""
    minute = ""
    inWords =""

    if  h:
        hour = time[h]
    
    if m:
        if m==15 or m==45:
            minute = "quarter"
            if m==15:
                minute += " past"
            elif m==45:
                minute += " to"
                hour = time[h+1] if h<12 else time[1]
        elif m == 30:
            minute = "half past"
        elif m > 0 and m < 30:
            minute_word = time[m]
            minute = f"{minute_word} minute{'s' if m!= 1 else ''} past"
        elif m > 30 and m < 60:
            minute_word = time[30-(m-30)]
            minute = f"{minute_word} minute{'s' if (30-(m-30))!= 1 else ''} to"
            hour = time[h+1] if h<12 else time[1]
    elif m == 0:
        minute = "o' clock"
        inWords = hour+" "+minute
        return inWords
        

    inWords = minute+" "+hour
    return inWords
    


print(timeInWords(5,31))