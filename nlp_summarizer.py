from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def summarize(text: str) -> str:
    # tokenize the text
    stop_words = set(stopwords.words("english"))
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
    
    # define average value for each sentence from given text
    sumVal = 0
    for sentence in sentence_freqTable:
        sumVal += sentence_freqTable[sentence]
    sentence_avg = sumVal // len(sentence_freqTable)

    # add sentences over 1.2 times the average value into our summary
    summary = ""
    for sentence in sentence_freqTable:
        if sentence_freqTable[sentence] > (1.2 * sentence_avg):
            summary += " " + sentence
    
    return summary






