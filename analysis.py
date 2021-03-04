
resultingDataFile = open("resulting_data.csv","w")


userDataFile = open("your_data.txt","r",encoding="utf-8")
resultingDataFile = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

positive_words = []
with open("positive.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open("negative.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

    
def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord

def get_pos(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences= strSentences.split()
    
    count=0
    for word in listStrSentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count+=1
    return count

def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)
    listStrSentences = strSentences.split()
    
    count=0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count+=1
    return count


def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  userDataFile.readlines()
    # headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        a=get_pos(listTD[0])
        b=get_neg(listTD[0])
        listTD=' '.join([str(elem) for elem in listTD]) 
        if b==1:
            print(str(listTD)+" (Negative text)")
        else:
            print(str(listTD)+" (Positive text)")
        resultingDataFile.write("{}, {}, {}".format(get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")


writeInDataFile(resultingDataFile)
userDataFile.close()
resultingDataFile.close()



