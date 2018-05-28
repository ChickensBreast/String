def CountWord(String, StringLen):
    CounterWord = 0
    for x in range(0, StringLen):
        if(String[x] == " "):
            CounterWord = CounterWord + 1
    CounterWord = CounterWord + 1
    return CounterWord

String = input("String = ")
StringLen = len(String)
CounterWord = CountWord(String, StringLen)
print(CounterWord)
WordArray = [""] * CounterWord

DebutMot = 0
NumberOfSpace = 0
LastWord = False
i = 0
x = 0
while(i < StringLen and x < CounterWord):
    if(String[i] == " "):
        if(NumberOfSpace == 0):
            WordArray[x] = String[DebutMot:i]
            DebutMot = i + 1
            NumberOfSpace = NumberOfSpace + 1
            print(NumberOfSpace)
                
        elif(NumberOfSpace != CounterWord):
            WordArray[x] = String[DebutMot:i]
            DebutMot = i + 1
            NumberOfSpace = NumberOfSpace + 1
            print(NumberOfSpace)
            if(NumberOfSpace == CounterWord -1):
                LastWord = True
        elif(LastWord == True):
            WordArray[x] = String[DebutMot:StringLen]
            NumberOfSpace = NumberOfSpace + 1
            print(NumberOfSpace)
        x = x + 1
    i = i + 1
for x in range(0, CounterWord):
    print(WordArray[x])