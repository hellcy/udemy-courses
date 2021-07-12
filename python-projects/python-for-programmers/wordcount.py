from os import write
import sys


def wordCount():
    if (len(sys.argv) < 2):
        print("File not provided.")
    else:
        try:
            file = open(sys.argv[1], "r")
            content = file.read()
            wordDict = readFile(content)
            writeFile(
                wordDict, "{}-count.txt".format(sys.argv[1].split('.')[0]))
        except Exception:
            print("File not found.")


def readFile(file):
    words = file.split(' ')
    totalWords = 0
    uniqueWords = 0

    wordDict = {}
    for word in words:
        if word not in wordDict.keys():
            wordDict[word] = 1
        else:
            wordDict[word] += 1
        totalWords += 1

    uniqueWords = len(wordDict)

    wordDict["total words"] = totalWords
    wordDict["unique words"] = uniqueWords
    return wordDict


def writeFile(wordDict, fileName):
    file = open(fileName, "w")
    content = ''
    content += "total words - {}\n".format(wordDict["total words"])
    content += "unique words - {}\n".format(wordDict["unique words"])

    del(wordDict["total words"])
    del(wordDict["unique words"])

    sortedList = sorted(wordDict.items(), key=lambda x: x[1], reverse=True)

    for item in sortedList:
        content += "{} - {}\n".format(item[0], item[1])

    file.write(content)


wordCount()
