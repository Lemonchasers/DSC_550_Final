import sys
import os
import json
import pickle

""" The workflow1.py file consists of a main function that requires two arguments
The first argument is the file path for a directory of wikipedia files. The second argument is 
the file path for pickled corpus.

The main function has two functions, one for getting a list of json files.
The second function reads json files. Then the main function dumps the data
as a pickled file.
"""



def main(input1,output2):

    def read_article_jsonl(file_path):
        records = []
        with open(file_path, 'r') as f:
            for line in f:
                records.append(json.loads(line))

        return records

    def read_jsonl_directory(directory):
        jsonl_file_paths = [
            entry.path
            for entry in os.scandir(directory) if entry.name.endswith('.jsonl')
        ]

        return jsonl_file_paths

    files = read_jsonl_directory(input1)

    records = []
    for i in files:
        y = read_article_jsonl(i)
        records.append(y)

    f = open(output2, 'wb')
    pickle.dump(records, f, -1)
    f.close()


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
