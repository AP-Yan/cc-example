# -*- coding: utf-8 -*-
# analyze tweets to get
# 1st: unique words and counts for each words
# 2nd: median value of numbers of unique words used each tweet
import os
import sys
import basicsorts

def AnaOneTweet(line):
    cur_words = {}
    # remove whitespace at the beginning of each line
    cur_line = line.lstrip(' ')
    # split line into words separeted by whitespace
    cur_line = cur_line.split() 
    for x in cur_line:
        # count the appearance of words in current line
        cur_words[x] = cur_words.get(x,0) + 1
    return cur_words

def Median(x):
    if len(x)%2 == 0:
        return (x[len(x)/2-1] + x[len(x)/2])/2.0
    else:
        return x[len(x)/2]

# change working direction
os.chdir(os.path.dirname(sys.argv[0]))
file_name = '../tweet_input/tweets.txt'
f = open(file_name, 'r', 0)
# initialization
words = {}
nUnique = []
median_value = []

if os.access(file_name, os.R_OK):
    with open(file_name) as f:
        # load & analyze data line by line
        for line in f:
            # analyze when input is not empty line
            if line.strip() != '':
                # figure out unique words and appearance in current line
                cur_words = AnaOneTweet(line)
                cur_count = len(cur_words.viewkeys())
                nUnique.append(cur_count)
                # sort current appearance number
                basicsorts.mergeSort(nUnique)
                median_value.append(Median(nUnique))
                # merge result in current line to the whole
                for i in cur_words.iterkeys():
                    words[i] = words.get(i,0) + cur_words[i]
                del cur_words
                del cur_count

# save unique words and appearance in ft1
with open('../tweet_output/ft1.txt', 'w') as f1:
    for key in sorted(words):
        f1.write('%-40s %9s\n'%(key, words[key]))

# save median vaules of unique word numbers in ft2
with open('../tweet_output/ft2.txt', 'w') as f2:
    for m in median_value:
        f2.write('%s\n'%m)