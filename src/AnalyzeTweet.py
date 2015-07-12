# analyze tweets to get
# 1st: unique words and counts for each words
# 2nd: median value of numbers of unique words used each tweet
import os
import sys
import basicsorts
from collections import Counter

def AnaOneTweet(line):
    cur_words = Counter()
    # split line into words separeted by whitespace
    cur_line = line.lstrip(' ').split()
    for x in cur_line:
        # count the appearance of words in current line
        cur_words[x] += 1
    return cur_words

def Median(x):
    # length of x is even
    if len(x)%2 == 0:
        return (x[len(x)/2-1] + x[len(x)/2])/2.0
    else:
        return x[len(x)/2]

def AnaTweet():
    # to current working dir
    os.chdir(os.path.dirname(sys.argv[0]))
    file_name = sys.argv[1]     
    # initialization
    words = Counter()
    nUnique = []
    median_value = []
    
    if os.access(file_name, os.R_OK):
        with open(file_name) as f:
            # load & analyze data line by line
            for line in f:
                # analyze when input is not empty line
                if line.strip() != '':
                    # find unique words and appearance in current line
                    cur_words = AnaOneTweet(line)
                    cur_count = len(cur_words.viewkeys())
                    nUnique.append(cur_count)
                    # sort current appearance number
                    basicsorts.mergeSort(nUnique)
                    median_value.append(Median(nUnique))
                    # merge result in current line to the whole
                    words.update(cur_words)
    return words, median_value

def saveTxt(words,median_value):
    file_name1 = sys.argv[2]
    # save unique words and appearance in ft1
    with open(file_name1, 'w') as f1:
        for key in sorted(words):
            f1.write('%-40s %9s\n'%(key, words[key]))
    
    file_name2 = sys.argv[3]
    # save median vaules of unique word numbers in ft2
    with open(file_name2, 'w') as f2:
        for m in median_value:
            f2.write('%s\n'%m)

if __name__ == "__main__":
    Out = AnaTweet()
    words = Out[0]
    median_value = Out[1]
    saveTxt(words,median_value)
    