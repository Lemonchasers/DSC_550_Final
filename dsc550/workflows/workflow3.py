import sys
import pickle
from functools import reduce
from collections import Counter
import operator



""" The workflow3.py file consists of a main function that requires two arguments
The first argument is the file path for a tokenized text that is the output of workflow2. The second argument is 
the file path for where to dump the top 10 pieces of text used in the tokenized text document. The export is report1.md
"""

def main(input1,output2):

    def count_words(document):
        words_to_count = reduce(operator.add, document)
        word_counts = Counter(words_to_count)
        return word_counts

    f = open(input1, 'rb')
    token_text = pickle.load(f)
    f.close()

    a = token_text[0:1000]


    t = count_words(a)

    p = t.most_common(10)

    newTemp = "Here is the top 10 counted values"+"\n"
    newTemp += str(p[0])+"\n"
    newTemp += str(p[1])+"\n"
    newTemp += str(p[2])+"\n"
    newTemp += str(p[3])+"\n"
    newTemp += str(p[4])+"\n"
    newTemp += str(p[5])+"\n"
    newTemp += str(p[6])+"\n"
    newTemp += str(p[7])+"\n"
    newTemp += str(p[8])+"\n"
    newTemp += str(p[9])+"\n"

    with open(output2, 'w') as output:
        output.write(newTemp)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
