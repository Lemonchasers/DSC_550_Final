import sys
import os
import json
import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score, accuracy_score, recall_score, f1_score, precision_score
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
#from sklearn.feature_extraction.decomposition import SparsePCA
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt


""" The workflow4.py file consists of a main function that requires two arguments
The first argument is the file path for a reddit file to be processed. The second argument is 
the file path for the dump of the processed reddit data.
"""



def main(input1,output2,output3):

    table = []
    with open(input1, 'r') as f:
        for line in f:
            table.append(json.loads(line))

    df = pd.DataFrame(table[0:10000])

    train_x, valid_x, train_y, valid_y = train_test_split(df.iloc[:,1], df.iloc[:,0])

    count_vect_con = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
    count_vect_con.fit(df.iloc[:,1])

    xtrain_count =  count_vect_con.transform(train_x)
    xvalid_count =  count_vect_con.transform(valid_x)
    model_l1 = LogisticRegression(penalty ='l1').fit(xtrain_count, train_y)
    l1_predictions = model_l1.predict(xvalid_count)

    filename = '/model1.pkl'
    pickle.dump(model_l1, open(output2+filename, 'wb'))

    model_l2 = LogisticRegression(penalty ='l2').fit(xtrain_count, train_y)
    l2_predictions = model_l2.predict(xvalid_count)

    filename = '/model2.pkl'
    pickle.dump(model_l2, open(output2+filename, 'wb'))

    model_nb = MultinomialNB().fit(xtrain_count, train_y)
    nb_predictions = model_nb.predict(xvalid_count)

    filename = '/model3.pkl'
    pickle.dump(model_nb, open(output2+filename, 'wb'))

    newTemp = "Here is the Logistic Regression penalty l1 model metrics"+"\n"
    newTemp += "Accuracy: "+str(accuracy_score(valid_y,l1_predictions))+"\n"
    newTemp += "AUC: "+str(roc_auc_score(valid_y,l1_predictions))+"\n"
    newTemp += "Precision: "+str(precision_score(valid_y,l1_predictions))+"\n"
    newTemp += "Recall: "+str(recall_score(valid_y,l1_predictions))+"\n"
    newTemp += "F1: "+str(f1_score(valid_y,l1_predictions))+"\n"
    newTemp += "\n"

    newTemp += "Here is the Logistic Regression penalty l2 model metrics"+"\n"
    newTemp += "Accuracy: "+str(accuracy_score(valid_y,l2_predictions))+"\n"
    newTemp += "AUC: "+str(roc_auc_score(valid_y,l2_predictions))+"\n"
    newTemp += "Precision: "+str(precision_score(valid_y,l2_predictions))+"\n"
    newTemp += "Recall: "+str(recall_score(valid_y,l2_predictions))+"\n"
    newTemp += "F1: "+str(f1_score(valid_y,l2_predictions))+"\n"
    newTemp += "\n"

    newTemp += "Here is the Naive Bayes model metrics"+"\n"
    newTemp += "Accuracy: "+str(accuracy_score(valid_y,nb_predictions))+"\n"
    newTemp += "AUC: "+str(roc_auc_score(valid_y,nb_predictions))+"\n"
    newTemp += "Precision: "+str(precision_score(valid_y,nb_predictions))+"\n"
    newTemp += "Recall: "+str(recall_score(valid_y,nb_predictions))+"\n"
    newTemp += "F1: "+str(f1_score(valid_y,nb_predictions))+"\n"
    newTemp += "\n"

    with open(output3, 'w') as output:
        output.write(newTemp)

if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])
