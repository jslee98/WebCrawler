""" Name : Jeffrey Lee
    Course : CSCI 203 Placement Test
    Assignment : Programming Project Part 1
    Date : 01/16/17 
    Note: Not using NumPy to display data. """

#Import

from hmc_urllib import getHTML

#Global Variables

MAX_WORDS = 25
DEPTH = 2

#Methods
            
def removeBoringWords(list):
    """ The removeBoringWords function removes all words from a list that
        appear in a list of words noted as "boring". The input is a list of
        strings. """
        
    """ Tests: ['a', 'and', 'iand', 'i', 'iss', 'was', 'too', 'to']
               ['A', '-a', '-the', 't-he', 'the', 'tHe', 'at', 'hat'] """
        
    stopWordList = ['a', 'i', 'and', 'is', 'was', 'has', 'for', 'are',
                    'of', 'the', 'or', 'as', 'to', 'an', 'in', 'on',
                    'this', 'had', 'it', 'at', 'be', 'to']
    for x in stopWordList:
        while x in list:
            list.remove(x)
            
def removePunctuation(list):
    """ The removePunctuation function removes all punctuation from a string.
        The input is a list of strings. """
        
    """ Tests: ['hey.', 'hey,howar.you', 'hi!mom', 'hell-o', 'sup?', '?whats?']
               ['...', 'hi.i', '(whats?)up', 'hi:0', 'remove>.<'] """
               
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range (0, len(list)):
        newWord = ''
        for x in range (0, len(list[i])):
            if list[i][x] in alphabet:
                newWord = newWord + list[i][x]
        list[i] = newWord
               
            
def removeNonWords(list):
    """ The removeNonWords function removes all strings that do not contain
        a vowel. The input is a list of strings. """
        
    """ Tests: ['---', 'aae', 'hey', 'blh', 'dltths']
               ['..h', 'hi', 'sspp', 'yes', 'n'] """

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for word in list:
        hasVowel = False
        for x in range (0, len(word)):
            if word[x] in vowels:
                hasVowel = True
        # If it doesn't have a vowl or is one letter (I and a are boring)
        if not hasVowel or len(word) == 1:
            list.remove(word)

def removeIng(list):
    """ The removeIng function removes the suffix -ing from a string.
        The input is a list of strings. """
        
    """ Tests: ['hovering', 'bring', 'handing']
               ['lovi.ng', 'bringing','string'] """
               
    vowels = ['a','e','i','o','u','y']
    for i in range (0, len(list)):
        word = list[i]
        #Checks to make sure 'ing' isn't in base word,
        # i.e.: bring, string
        baseWord = word[0:len(word) - 3]
        hasVowel = False
        for x in range (0, len(baseWord)):
            if baseWord[x] in vowels:
                hasVowel = True
        # Removes -ing if not in base word
        # If base word ends in v, replaces -ing with e
        # Removes double letter if added for suffix
        if word[len(word)-3:len(word)] == 'ing' and hasVowel:
            if word[len(word) - 4] == word[len(word) - 5]:
                list[i] = list[i][0:len(word)-4]
            elif word[len(word) - 4] == 'v':
                list[i] = list[i][0:len(word) - 3] + 'e'
            else:
                list[i] = list[i][0:len(word) - 3]
                
def removeEd(list):
    """ The removeEd function removes the past tense suffix -ed from a string.
        The input is a list of strings. """
        
    """ Tests: ['dead', 'daed', 'bed', 'extracted']
               ['.e.d', 'head', 'madeed'] """
    
    exceptions = ['bed', 'led']
    for i in range (0, len(list)):
        word = list[i]
        if word[len(word) - 2:len(word)] == 'ed' and \
           word not in exceptions:
            if word[len(word) - 3] == word[len(word) - 4]:
                list[i] = list[i][0:len(word) - 3]
            # If base word ends in I, replace with Y
            # i.e. carried becomes carry
            elif word[len(word) - 3] == 'i':
                list[i] = list[i][0:len(word) - 3] + 'y' 
            else:
                list[i] = list[i][0:len(word) - 2]

def removeEr(list):
    """ The removeEr function removes the suffix -er from a string.
        The input is a list of strings. """
        
    """ Tests: ['hover', 'loveer', 'mother']
               ['lov.er', 'love.r','smotherer'] """
               
    exceptions = ['number', 'computer', 'another', 'mother', 'father', 'hover'
                  'hammer', 'liver', 'other']
    for i in range (0, len(list)):
        word = list[i]
        if word[len(word) - 2:len(word)] == 'er' and \
           word not in exceptions:
            if word[len(word) - 3] == word[len(word) - 4]:
                list[i] = list[i][0:len(word) - 3]
            elif word[len(word) - 3] == 'v':
                list[i] = list[i][0:len(word) - 2] + 'e'
            else:
                list[i] = list[i][0:len(word) - 2]
                
def removePlural(list):
    """ The removePlural function removes the plural suffix -s from a string.
        The input is a list of strings. """
        
    """ Tests: ['stars', 'sss', 'sass', 'glass']
               ['hands', 'glands', 'protrudes', 'trend.s'] """
        
    exceptions = ['this', 'his', 'bias', 'alias', 'analysis', 'basis',
                  'diagnosis', 'octopus', 'cactus', 'hypnosis', 'campus']    
    for i in range (0, len(list)):
        word = list[i]
        if word[len(word) - 1:len(word)] == 's' and \
           word[len(word) - 2:len(word)] != 'ss' and \
           word not in exceptions:
               list[i] = list[i][0:len(word) - 1]

def cleanList(list):
   """ The cleanList function cleans a list of strings by executing three
       functions to remove punctuation, non-words, and boring words.
       The input is a list of strings. """
       
   """ Test: ['i.', '.i', 'br.ng', 't.h.i.s'] """
       
   removePunctuation(list)
   removeNonWords(list)
   removeBoringWords(list)
               
def stemList(list):
    """ The stemList function executes four stemming methods to simplify words
        to their base form. The input is a list of strings. """
    
    """ Test: ['beds', 'weddings', 'hammers', 'headeding'] """
    
    removePlural(list)
    removeIng(list)
    removeEd(list)
    removeEr(list)
    
def wordCounter(list):
    """ The wordCounter function creates a list of strings and a list of
        integers in parallel, and counts how many times each word appears.
        The input is a list of strings. """
    
    """ Test: ['yes', 'yes' 'yes', 'yes', 'no', 'one', 'no'] """
    
    listOfWords = [list[0]]
    listOfOccur = [1]
    for i in range (1, len(list)):
        if list[i] not in listOfWords:
            # if word is not already in list, adds word to word list and
            # adds 1 to end of occurence counting list
            listOfWords.append(list[i])
            listOfOccur.append(1)
        else:
            # if word is already in word list, adds 1 to num of occurences
            for x in range (0, len(listOfWords)):
                if list[i] == listOfWords[x]:
                    listOfOccur[x] = listOfOccur[x] + 1
    return (listOfWords,listOfOccur)
            
def wordSorter(listTuple):
    """ The wordSorter function takes a parellel list tuple and sorts
        the first list of strings in accordance to the parallel second list 
        of integers. It also shortens the lists to the global limit MAX_WORDS
        so as to not crowd the console. The input is a two-tuple of lists, the 
        first being strings and the second being integers. """
        
    """ Test: (['yes', 'hello' 'no', 'four', 'seven', 'eleven'], 
              [1, 3, 7, 0, 1, 4]) """
        
    wordList = listTuple[0]
    numList = listTuple[1]
    for i in range (0, len(numList)):
        maxOccur = max(numList[i:])
        maxIndex = numList[i:].index(maxOccur)
        maxOccurWord = wordList[i + maxIndex]
        numList[i + maxIndex] = numList[i]
        wordList[i + maxIndex] = wordList[i]
        numList[i] = maxOccur
        wordList[i] = maxOccurWord
    return (wordList[0:MAX_WORDS], numList[0:MAX_WORDS])

def printDictionary(listTuple):
    """ The printDictionary function prints a parallel list tuple in the format
        provided in the assignment. The input is a two-tuple of lists. """
        
    dictionaryString = "{ \'"+ listTuple[0][0] + "\'" + \
    " : " + str(listTuple[1][0])
    for i in range (1, len(listTuple[0])):
        dictionaryString = dictionaryString + ", \'" + \
        listTuple[0][i] + "\'" + " : " + str(listTuple[1][i])
    print ('Here is the dictionary of words on that page:')
    print (dictionaryString + ' }')

def printTextCloud(sortedListTuple):
    """ The printTextCloud function prints a parallel list tuple in the format
        provided in the assignment. The input is a two-tuple of lists. """
        
    print('Here is the text cloud for your web page:')
    for i in range (0, len(sortedListTuple[0])):
         print(sortedListTuple[0][i] + ' (' + str(sortedListTuple[1][i])  + ')')                 

def webCrawl(urlList, pagesDeep, listOfWords, listOfCrawled):
    """ The webCrawl function is a recursive method that returns a list of
        strings from pages a given distance away from the starting URL. The
        pages do not repeat themselves. The inputs are a list of URLs, the 
        "depth" or distance away from the first URL, a list of strings
        compiled from URLs that have already been crawled, and a list of
        URLs that have already been crawled. """
        
    """ Test: webCrawl at DEPTH = 0 for the three test pages. Then, webCrawl at
        DEPTH = 1 for test page 2. The result should be a simple addition of
        all three pages. """
    
    if pagesDeep == DEPTH:
        return listOfWords
    else:
        pagesDeep = pagesDeep + 1
        newUrlList = []
        for url in urlList:
            if url not in listOfCrawled:
                listOfWords = listOfWords + getHTML(url)[0].split()
                listOfCrawled.append(url)
                for x in getHTML(url)[1]:
                    if x not in newUrlList:
                        newUrlList.append(x)
        return webCrawl(newUrlList, pagesDeep, listOfWords, listOfCrawled)
            
             
# Execution

inputUrl = input("Enter URL to analyze: ")
while inputUrl[0:7] != 'http://':
    inputUrl = input("Invalid URL. Please ensure URL begins with 'http://': ")
    

wordList = getHTML(inputUrl)[0].split()
crawledUrls = [inputUrl]
wordList = webCrawl(getHTML(inputUrl)[1], 0, wordList, crawledUrls)

cleanList(wordList)
stemList(wordList)
removeBoringWords(wordList)
removeNonWords(wordList)

sortedListTuple = wordSorter(wordCounter(wordList))
print('')
printDictionary(sortedListTuple)
print('')
printTextCloud(sortedListTuple)
