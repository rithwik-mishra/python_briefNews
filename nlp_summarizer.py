from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

def summarize(long_text: str) -> str:
    """Algorithm that summarizes long text into an 8 sentence summary using a 5 step process."""
    # 1. tokenize the text
    stop_words = stopwords.words("english")
    words = word_tokenize(long_text)
    sentences = sent_tokenize(long_text)

    # 2. create a frequency table to count each word
    word_freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        if word in word_freqTable:
            word_freqTable[word] += 1
        else:
            word_freqTable[word] = 1

    # 3. define weighted value for each word from given text
    max_freq = max(word_freqTable.values())
    for word in word_freqTable:
        word_freqTable[word] /= max_freq
    
    # 4. create a frequency table to count each sentence
    sentence_freqTable = dict()
    for sentence in sentences:
        for word, freq in word_freqTable.items():
            if word in sentence.lower():
                if sentence in sentence_freqTable:
                    sentence_freqTable[sentence] += freq
                else:
                    sentence_freqTable[sentence] = freq    

    # 5. use heap queue to extract top 8 largest weighted values and display as summary
    summary_top8 =  heapq.nlargest(8, sentence_freqTable, key = sentence_freqTable.get) 
    summary = " ".join(summary_top8)
    return summary