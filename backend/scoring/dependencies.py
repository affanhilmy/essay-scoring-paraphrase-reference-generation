import math
import string
import numpy as np

def lcs(S1, S2, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    # Building the mtrix in bottom-up way
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]

    lcs = [""] * (index+1)
    lcs[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if S1[i-1] == S2[j-1]:
            lcs[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs

def preprocessing(text, outputTokenize=False):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.strip()

    if outputTokenize:
        result = ' '.join(char for char in text)
    else:
        result = text

    return result

def GANLCS(answer, reference, max_score):
    source = preprocessing(answer)
    reference = preprocessing(reference)
    m = len(reference)
    n = len(source)
    lcs_value = lcs(reference, source, m, n)
    lcs_value = [x for x in lcs_value if x] #remove empty list in array
    lcs_len = len(lcs_value)

    # GAN-LCS equation
    if lcs_len == 0:
        ganLCS = 0
    else:
        ganLCS = (2 * math.sqrt(m * n)/(m + n)) * math.exp( math.log((lcs_len) / n, 10))

    ganLCS = ganLCS*max_score

    return ganLCS

def get_scores(answers, references, max_score):
    scores = []
    for answer in answers:
        temp_scores = []
        for reference in references:
            temp_scores.append(GANLCS(answer, reference, max_score))
        scores.append(np.max(temp_scores))
        
    return scores