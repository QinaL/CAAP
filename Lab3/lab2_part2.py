import math

def count_tokens(tokens):
    '''
    Takes a list of tokens and returns a dictionary with the counts of each token
    Input: list
    Return: dictionary
    '''
    tokenCount = {}
    for token in tokens:
        if token not in tokenCount:
            tokenCount[token] = 0
        tokenCount[token] += 1
    return tokenCount

def find_top_k(tokens, k):
    '''
    Takes a list of tokens and a non-negative integer k and returns the k tokens 
    that occur most frequently in the list
    Input: list, int
    Return: list
    '''
    counts = count_tokens(tokens) 
    counts = sorted(counts, key = lambda token: counts[token], reverse = True)
    return counts[:k]

def find_min_count(tokens, minNum):
    '''
    Takes a list of tokens and returns a list of the tokens that have occcured at least 
    minNum number of times in the list
    Input: list, int
    Return: list
    '''
    counts = count_tokens(tokens)
    mins = []
    for token, count in counts.items():
        if count >= minNum:
            mins.append(token)
    return mins
    
def tf(token, document):
    '''
    Computes the augmented frequency of token in document
    Input: string, list
    Return: int
    '''
    counts = count_tokens(document)
    f = counts[token]
    topToken = find_top_k(document, 1)[0]
    return 0.5 + 0.5 * (f/counts[topToken])
    
def idf(token, documents):
    '''
    Computes the inverse document frequency of token in documents (which is a collection of documents)
    Input: string, list of lists
    Return: int
    '''
    numDocsInCol = len(documents)
    # print(numDocsInCol)
    numTokenAppears = 0
    for doc in documents:
        if token in doc:
            numTokenAppears += 1
    # print(numTokenAppears)
    return math.log(numDocsInCol/numTokenAppears)

def salient(d, D, T):
    '''
    Takes a document (d), a collection of documents (D), and a threshold (T), and 
    return the tokens in d that are salient as a set
    Input: list of tokens, list of lists (of tokens), float
    Return: set
    '''
    salientWords = []
    for token in d:
        tf_idf = tf(token, d) * idf(token, D)
        if tf_idf > T:
            salientWords.append(token)
    return set(salientWords)



def main():
    tokens = ['A', 'B', 'C', 'A']
    tokens2 = ['D', 'B', 'C', 'D', 'D', 'B', 'D', 'C', 'D', 'A']
    count = count_tokens(tokens)
    print(find_top_k(tokens2, 2))
    print(find_min_count(tokens2, 2))
    D = [['D', 'B', 'D', 'C', 'D', 'C', 'C'],
        ['D', 'A', 'A'],
        ['D', 'B'], #our dummy tokens are just letters
        []] 
    print(tf('B', D[0]))
    print(idf('A', D))
    print(salient(D[0], D, 0.4))

if __name__ == "__main__":
    main()
