from os import listdir
from os import popen
from os.path import isfile, join
import nltk
import string
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

mypath = 'data/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

file_paths = ['cleaned_'+mypath+f for f in onlyfiles]

pickle_in = open("vectorizer.pickle","rb")
vectorizer = pickle.load(pickle_in)

n = 10
pickle_in = open("tags_dict.pickle","rb")
post_tags_dict = pickle.load(pickle_in)

i = 1
import sys
feature_array = np.array(vectorizer.get_feature_names())

feature_array = np.array(vectorizer.get_feature_names())

print(sys.argv[1])
print(sys.argv[2])
print(type(int(sys.argv[1])))
print(type(int(sys.argv[2])))

i = int(sys.argv[1])
for file_name in onlyfiles[int(sys.argv[1]):int(sys.argv[2])]:
    file = file_paths[i]
    print('file '+ str(i) + ' of ' + str(len(onlyfiles)))
    print(sys.getsizeof(feature_array), sys.getsizeof(post_tags_dict))
    #i += 1
    X =  vectorizer.transform([file])
    tfidf_sorting = np.argsort(X.toarray()).flatten()[::-1]
    top_n = feature_array[tfidf_sorting][:n]
    post_tags_dict[file_name] = top_n
    print(sys.getsizeof(tfidf_sorting), sys.getsizeof(top_n), sys.getsizeof(X))
    del top_n
    del X
    del tfidf_sorting
    i+=1
    

pickle_out = open("tags_dict.pickle","wb")
pickle.dump(post_tags_dict, pickle_out)
pickle_out.close()