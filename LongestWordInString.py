msg=input("Enter a message:")
wordList=[]
i=0
word=""
while i<len(msg):
    if msg[i]!=" ":
        word += msg[i]
    else:
        wordList.append(word)
        word=""
    i += 1
wordList.append(word)
longestWord=""
for each in wordList:
    if len(each)>len(longestWord):
        longestWord=each
print("The longest word in your message is:",longestWord)