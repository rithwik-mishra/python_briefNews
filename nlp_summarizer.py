from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

def summarize(text: str) -> str:
    # tokenize the text
    stop_words = stopwords.words("english")
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    # create a frequency table to count each word
    word_freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in word_freqTable:
            word_freqTable[word] += 1
        else:
            word_freqTable[word] = 1
    
    # create a frequency table to count each sentence
    sentence_freqTable = dict()
    for sentence in sentences:
        for word, freq in word_freqTable.items():
            if word in sentence.lower():
                if sentence in sentence_freqTable:
                    sentence_freqTable[sentence] += freq
                else:
                    sentence_freqTable[sentence] = freq
    
    # define weighted value for each sentence from given text
    sumVal = 0
    for sentence in sentence_freqTable:
        sumVal += sentence_freqTable[sentence]
    sentence_avg = sumVal // len(sentence_freqTable)

    # use heap queue to extract top 8 largest weighted values and display as summary
    summary_top8 =  heapq.nlargest(8, sentence_freqTable, key = sentence_freqTable.get) 
    summary = " ".join(summary_top8)
    return summary
