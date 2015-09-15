"""
Shippable 
"""
import sys
from textblob import TextBlob
reload(sys)
sys.setdefaultencoding('utf8')

filetoopen = open('filename.txt', 'r')

lines = filetoopen.readlines()

for line in lines:
    line = line.encode('utf-8')
    blob = TextBlob(line)
    phrases = blob.noun_phrases
    print str(phrases)
