import re
import statistics

#prompt user to pick paragraph
option = input('Analyze which paragraph? Enter 1 or 2 or 3:')

#open right .txt file and store
file = open('Paragraph_' + option + '.txt', 'r') 
my_text = file.read()

#count words, sentences
words = re.split(' |-', my_text)
num_words = len(words)
sentences = re.split("(?<=[.!?]) +", my_text)
num_sent = len(sentences)

#initialize list to be averaged
wordlengths = []

#create list
for word in words:
    wordlengths.append(len(word))
    
#perform mean word length calculation and avg. sentence length 
avg_word = round(statistics.mean(wordlengths),1)
avg_sent = num_words/num_sent

#create message
message = 'Paragraph Analysis\n\
-----------------\n\
Approximate Word Count: {}\n\
Approximate Sentence Count: {}\n\
Average Letter Count: {}\n\
Average Sentence Length: {}'\
.format(num_words,num_sent,avg_word,avg_sent)

#print to terminal
print(message)
