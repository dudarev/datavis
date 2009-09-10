# calculates words frequency for a specified file
# format:
# python word_count_list.py file_name.txt

from optparse import OptionParser
parser = OptionParser()
(options, args) = parser.parse_args()

# check that file to count words is specified
if(len(args)<1):
    print """please specify files to count words:
python words_count_list.py filename.txt"""
    raise SystemExit

try:
    input = open(args[0], 'r')
except IOError:
    print "file '%s' cannot be open" % args[0]
    raise SystemExit

from string import punctuation
import re

numbers_re = re.compile('[0-9]')

text = input.read()
wordlist = text.split()
dictionary = dict()
total_word = 0
for word in wordlist:
    word = word.strip(punctuation).lower()
    if word and not numbers_re.match(word):
        if dictionary.has_key(word): 
            dictionary[word]=dictionary[word]+1
        else:
            dictionary[word]=1
        total_word += 1

# save words count in reverse frequency order (more frequent -- first)
aux = [(dictionary[key], key) for key in dictionary]
aux.sort()
aux.reverse()
f = open('word_count_list.txt','w')
for a in aux: 
    f.write("%s %s\n" % (a[1],a[0]))
