def count_tokens(tokens):
    tokenCount = {}
    for token in tokens:
        if token not in tokenCount:
            tokenCount[token] = 0
        tokenCount[token] += 1
    return tokenCount

def find_top_k(tokens, k):
    counts = count_tokens(tokens) 
    counts = sorted(counts, key = lambda token: counts[token], reverse = True)
    return counts[:k]

def find_min_count(tokens, num):
    counts = count_tokens(tokens)
    mins = []
    for token, count in counts.items():
        if count >= num:
            mins.append(token)
    return mins
    


def main():
    tokens = ['A', 'B', 'C', 'A']
    tokens2 = ['D', 'B', 'C', 'D', 'D', 'B', 'D', 'C', 'D', 'A']
    count = count_tokens(tokens)
    print(find_top_k(tokens2, 2))
    print(find_min_count(tokens2, 2))
    pass

if __name__ == "__main__":
    main()