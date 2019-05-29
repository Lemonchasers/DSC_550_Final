import sys
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import pickle



""" The workflow2.py file consists of a main function that requires two arguments
The first argument is the file path for a corpus that is the output of workflow1. The second argument is 
the file path for where to dump the tokenized text.

The main function has two functions, one for getting a list of json files.
The second function reads json files. Then the main function dumps the data
as a pickled file.
"""

nltk.download('punkt')

def main(input1,output2):

    def tokenize_document(document):
        tokens=nltk.sent_tokenize(document)
        return tokens

    def tokenize_documents(all_documents):

        text_to_tokenize = []

        for i in all_documents:
            for x in i:
                text = x.get('section_texts')
                s = len(text)
                for num in range(s):
                    s2 = text[num]
                    text_to_tokenize.append(s2)

        return text_to_tokenize

    f = open(input1, 'rb')
    mydict = pickle.load(f)
    f.close()

    t = tokenize_documents(mydict)

    token_text = []
    for i in t:
        y = tokenize_document(i)
        token_text.append(y)

    f = open(output2, 'wb')
    pickle.dump(token_text, f, -1)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
